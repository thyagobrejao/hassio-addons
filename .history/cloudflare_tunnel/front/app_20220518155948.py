from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('hello.html', name=name)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
