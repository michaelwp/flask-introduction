from flask import Flask, jsonify, request, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)

# setup cors
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

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
    header = 'Rest API Introduction'
    return render_template('index.html',header=header), 200


@app.route('/emails')
def get_emails():
    return jsonify(response), 200


@app.route('/emails', methods=['POST'])
def add_email():
    emails.append(request.get_json()["email"])
    return jsonify(response), 201


# run the application
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True, port=5000, threaded=True)
