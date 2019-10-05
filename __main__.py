# -*- coding: utf-8 -*-

from flask import Flask
import peewee
from flask import Flask, jsonify, request
from flask_cors import CORS
import main


app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return "Oi mundo"

# GET /postagens/
@app.route('/bot')
def postagens():
    #return jsonify([postagem.to_dict() for postagem in Postagem.select()])
    return "response"


# POST /postagens/
@app.route('/voce', methods=['POST'])

def nova_postagem():
    cont = 0

    message =request.form.get('message')
    # titulo.headers.add('Access-Control-Allow-Origin', '*')
    # titulo.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    # titulo.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    message = str(message)
    anwser = main.StartBot(message)
    return jsonify({'status': 200, 'anwser': anwser})


if __name__ == '__main__':
    app.run(debug=True)#
    app.run(debug=True, port=6543)