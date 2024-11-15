from flask import Flask

# create flask app instance
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World !"

app.run('0.0.0.0')