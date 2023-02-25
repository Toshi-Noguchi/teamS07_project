from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
#データベースの設計
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///map.db'
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String, nullable=False)
    accountname = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)


@app.route("/")
def home():
    return render_template('post.html')


if __name__ == "__main__":
    app.run()