from flask import Blueprint
from api.controllers import email, home

bp = Blueprint('router', __name__)


@bp.route("/", methods=["GET"])
def Home():
    return home.Home()


@bp.route("/emails", methods=["GET"])
def GetEmails():
    return email.GetEmails()


@bp.route("/emails", methods=["POST"])
def AddEmail():
    return email.AddEmail()
