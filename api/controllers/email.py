from flask import jsonify, request
from api.controllers.common import Response

emails = [
    'stevenxx@mail.com'
    , 'stivanxx@mail.com'
    , 'keziaxx@mail.com'
    , 'sheriaxx@mail.com'
]


def GetEmails():
    return jsonify(Response(emails)), 200


def AddEmail():
    emails.append(request.get_json()["email"])
    return jsonify(Response(emails)), 201
