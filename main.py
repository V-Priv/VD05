from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def about():
    return render_template("about.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/base")
def base():
    return render_template("base.html")


if __name__ == "__main__":
    app.run()
