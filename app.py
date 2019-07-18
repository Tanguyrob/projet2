from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello second projet"

@app.route("/next")
def seconde_fct():
    return "hello seconde fonction"

if __name__ == '__main__':
    app.run()