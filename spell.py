from flask import Blueprint

spell_bp = Blueprint('spell_bp', __name__,
    template_folder='templates',
    static_folder='static')

@spell_bp.route('/baz.bar')
def foo():
    pass
