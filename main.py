from flask import Flask, jsonify, request

app = Flask(__name__)

emails = [
    'stevenxx@mail.com'
    , 'stivanxx@mail.com'
    , 'keziaxx@mail.com'
    , 'sheriaxx@mail.com'
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
