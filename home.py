from flask import Blueprint

home_bp = Blueprint('home_bp', __name__,
    template_folder='templates',
    static_folder='static')

@home_bp.route('/baz.bar')
def foo():
    pass
