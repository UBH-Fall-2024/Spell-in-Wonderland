from flask import Blueprint

app = Flask(__name__)

from home import home_bp
from spell import spell_bp

app.register_blueprint(home_bp)
app.register_blueprint(spell_bp)