from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:test@cluster0.plgtff3.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/members', methods=["GET"])
def send_members():
   members = list(db.member.find({}, {'_id': 0, 'id': 1, 'name': 1, 'profile': 1, 'mbti': 1}))
   return jsonify({'members': members})

@app.route('/member/<id>')
def send_template(id):
    return render_template('./template.html', id=id)

@app.route('/member/detail/<id>')
def send_detail(id):
   id = int(id)
   member = dict(db.member.find_one({'id': id}, {'_id': False}))
   return jsonify({'member': member})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)