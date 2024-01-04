from flask import Flask, jsonify, request

app = Flask(__name__)

emails = [
    'stevennanda38@gmail.com'
    , 'stivannuslambaihang1@gmail.com'
    , 'kezialpn@gmail.com'
    , 'sheriaamaria24@gmail.com'
]

response = {
    'status': 'success'
    , 'data': emails
}


@app.route("/")
def hello_world():
    return "Hello, World!", 200


@app.route('/emails')
def get_incomes():
    return jsonify(response), 200


@app.route('/emails', methods=['POST'])
def add_income():
    emails.append(request.get_json()["email"])
    return jsonify(response), 201