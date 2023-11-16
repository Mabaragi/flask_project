from flask import Blueprint, current_app

bp = Blueprint('main', __name__, url_prefix='/')


@bp.route('/hello')
def hello_pybo():
    return 'Hello, Blueprint!'


@bp.route('/')
def index():
    db = current_app.db
    return str(db)
