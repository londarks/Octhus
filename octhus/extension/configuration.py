from importlib import import_module
from dynaconf import FlaskDynaconf

def load_extensions(app):
    for extension in app.config.EXTENSIONS:
        load = import_module(extension)
        load.init_app(app)

def init_app(app):
	FlaskDynaconf(app)