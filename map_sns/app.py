from flask import Flask, render_template
import sqlite3


app = Flask(__name__)
#データベースの設計
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('mapSNS.db')
    
    return g.db



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