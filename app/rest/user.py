from flask import Response, Blueprint
# from app.app import db

user_blueprint = Blueprint('user', __name__ , url_prefix='/user')


@user_blueprint.route('/hello')
def hello():
    return Response('message')