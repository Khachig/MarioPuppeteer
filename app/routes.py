from flask import render_template, flash, request, redirect, url_for
from wtforms import Form, TextField, validators
from app import app


class CommandForm(Form):
    # Command field
    command = TextField("Command:", validators=[validators.required()])

    @app.route("/", methods=["GET", "POST"])
    @app.route("/index")
    def index():
        form = CommandForm(request.form)

        if request.method == "POST":
            command = request.form["command"]
            # Perform field validation, then flash field content
            if form.validate():
                flash("Command: " + command)
                # Redirect back to same page with empty field
                return redirect(url_for("index"))

        # Render index.html
        return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run()
