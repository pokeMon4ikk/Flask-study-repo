from flask import Flask

from BlogApp.articles.views import article
from BlogApp.users.views import user
from BlogApp.index.views import index
from BlogApp.report.views import report

VIEWS = [
    index,
    user,
    article,
    report
]


def create_app() -> Flask:
    app = Flask(__name__)
    register_blueprints(app)
    return app


def register_blueprints(app: Flask):
    for view in VIEWS:
        app.register_blueprint(view)
