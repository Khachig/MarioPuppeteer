from flask import render_template, flash, request, redirect, url_for
from wtforms import Form, TextField, validators
from app import app
from os import path


class CommandForm(Form):
    # Command field
    command = TextField("Command:", validators=[validators.required()])

    @staticmethod
    def write_command(cmd):
        # Game commands and their corresponding memory address/value pairs
        mario_commands = {'jump':'0x009F 0xFB', 'highjump':'0x009F 0xF8', 'time':'0x07F8 0x09',
                          'lives':'0x075A 0x80', 'big':'0x0754 0x00'}

        # Path to root directory of app
        root_directory = path.dirname(app.root_path)
        filepath = path.join(root_directory, "luascript", "commands.txt")

        with open(filepath, "w") as cmd_file:
            # Try to write the corresponding memory address/value to commands.txt
            try:
                cmd_file.write(mario_commands[cmd])
                cmd_file.write("\n")
                flash(f"Command [{cmd}] written to memory!")
                return 0
            except KeyError:
                flash(f"Command [{cmd}] not found!")
                return 1


    @app.route("/", methods=["GET", "POST"])
    @app.route("/index")
    def index():

        # Form object
        form = CommandForm(request.form)

        if request.method == "POST":
            command = request.form["command"]
            # Perform field validation, then write command to file
            if form.validate():
                CommandForm.write_command(command)
                # Redirect back to same page with empty field
                return redirect(url_for("index"))

        # Render index.html
        return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run()
