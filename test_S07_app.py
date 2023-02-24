from flask import Flask,render_template
app = Flask(__name__, static_folder='.',static_url_path='')

@app.route('/login')
def login():
    return render_template("login.html")