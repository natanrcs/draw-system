import os

from flask import Flask, flash, redirect, render_template, request, url_for

from draw import load_names
from service import get_result

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "dev-only-change-me")

NAMES_PATH = "data.txt"
DRAWS_PATH = "draws.json"
CATEGORIES = ["chocolate", "havaianas"]


def find_name(typed, names):
    lookup = {name.lower(): name for name in names}
    return lookup.get(typed.strip().lower())


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        selected = request.form.get("category", "")
        typed = request.form.get("name", "")
        names = load_names(NAMES_PATH)
        name = find_name(typed, names)

        if selected not in CATEGORIES:
            flash("Categoria inválida.", "error")
            return redirect(url_for("home"))

        if name is None:
            flash("Nome não encontrado na lista de funcionários.", "error")
        else:
            try:
                friend = get_result(selected, name, names, DRAWS_PATH)
                flash(f"{name}, seu amigo {selected} é {friend}.", "result")
            except ValueError as exc:
                flash(str(exc), "error")

        return redirect(url_for("home", category=selected))

    selected = request.args.get("category", CATEGORIES[0])
    if selected not in CATEGORIES:
        selected = CATEGORIES[0]

    return render_template("index.html", categories=CATEGORIES, selected=selected)


if __name__ == "__main__":
    app.run(debug=True)
