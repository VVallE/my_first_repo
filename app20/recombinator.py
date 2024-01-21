from flask import Flask, render_template, request
from random import shuffle
app = Flask(__name__)


@app.route("/")
@app.route("/main")
def index():
    return render_template("index.html")


@app.route("/recombination", methods=["GET", "POST"])
def recombination():
    result = None
    if request.method == "POST":
        word = request.form.get("word", "")
        result = shuffle_word(word)
    return render_template("recombination.html", result=result)


def shuffle_word(word):
    word = list(word)
    shuffle(word)
    res = "".join(word)
    return res


if __name__ == "__main__":
    app.run(debug=True)
