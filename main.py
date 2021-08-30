from flask import Flask


app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>working fine </h1>"


app.run(debug=True)