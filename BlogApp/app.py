from flask import Flask, render_template
from BlogApp.views.users import users_app
from BlogApp.views.articles import articles_app

app.register_blueprint(users_app, url_prefix="/users")
app.register_blueprint(articles_app, url_prefix="/articles")


app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

