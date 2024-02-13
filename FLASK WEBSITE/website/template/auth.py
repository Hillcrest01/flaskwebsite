from flask import Blueprint
auth = Blueprint('views', __name__)


@auth.route('/login')
def login():
    return "login"

@auth.route('/logout')
def logout():
    return "Logout"

@auth.route('/sign-up')
def sign_up():
    return "sign-up"