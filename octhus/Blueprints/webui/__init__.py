from flask import Blueprint
from octhus.Blueprints.webui.view import *

bp = Blueprint("webui", __name__, template_folder="templates",
								  static_folder="static",
								  static_url_path="/")

bp.add_url_rule('/', 'index', index)
bp.add_url_rule('/season', 'season', season, methods=["GET","POST"])
bp.add_url_rule('/releases', 'releases' , releases)
# bp.add_url_rule('/setSeason','changeSeason' ,changeSeason, methods=["POST"])


def init_app(app):
    app.register_blueprint(bp)