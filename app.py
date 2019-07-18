from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Hello second projet</h1>"

@app.route("/next")
def seconde_fct():
    return "hello seconde fonction"

if __name__ == '__main__':
    app.run()