from flask import Flask
import db

app = Flask(__name__)


@app.route("/")
def hello_world():
    user = db.get_users()
    return "<p>"+user.nickname+"</p>"
