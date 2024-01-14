from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/spam/<string:text>/<int:count>")
def spam(text="spam", count=10):
    text = " " + text
    return text * count


@app.route("/")
@app.route("/main")
def index():
    return render_template("index.html")


@app.route("/registration")
def registration():
    return render_template("form.html")


@app.route("/submit_form", methods=["POST"])
def submit_form():
    if request.method == "POST":
        value = int(request.form.get("age"))
        if value < 18:
            return f"Ваш вік менше 18, ми не зможемо <strike>обдурити вас</strike> вам допомогти"
        else:
            return render_template("scam.html")  # TODO реалізувати цей шаблон


if __name__ == "__main__":
    app.run(debug=True)
