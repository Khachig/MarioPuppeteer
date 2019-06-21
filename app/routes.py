from os import path
from random import choice

from flask import flash, redirect, render_template, request, url_for
from wtforms import Form, TextField, validators

from app import app


class CommandForm(Form):
    # Command field
    command = TextField("Command:", validators=[validators.required()])

    # Game commands and what they do
    commands_help = {"Commands are case insensitive":"",
                     "Command":         "Explanation",
                     "Jump":            "Mario jumps",
                     "Highjump":        "Mario jumps very high",
                     "Time":            "Time is maxed out",
                     "Invincible":      "Mario becomes invincible",
                     "Fly":             "Mario can fly",
                     "Colour":          "Background changes colour randomly",
                     "lookL":           "Mario turns left",
                     "lookR":           "Mario turns right",
                     "runL":            "Mario runs left",
                     "runR":            "Mario runs right",
                     "Warp":            "Mario warps to a different region",
                     "Lives":           "Mario has maximum lives",
                     "Revive":          "Mario revives from death (only works before screen goes black)",
                     "Big":             "Mario turns big"}

    @staticmethod
    def write_command(cmd):

        # Path to root directory of app
        root_directory = path.dirname(app.root_path)
        filepath = path.join(root_directory, "luascript", "commands.txt")

        # Game commands and their corresponding memory address/value pairs
        mario_commands = {"jump":"0x009F 0xFB", "highjump":"0x009F 0xF8", "time":"0x07F8 0x09",
                          "invincible":"0x079F 0xFF", "fly":"0x0704 0x01", "colour":"0x0773 0x0",
                          "lookl":"0x0033 0x02", "lookr":"0x0033 0x01", "runr":"0x0057 0x64",
                          "runl":"0x0057 0xA0", "warp":"0x000E 0x03", "lives":"0x075A 0x80",
                          "revive":"0x000E 0x08", "big":"0x0754 0x00"}

        # List of values to be randomly appended to the colour code
        colour_values = ["0", "1", "2", "3", "4", "9", "A", "B", "C", "D", "E", "F"]

        with open(filepath, "w") as cmd_file:
            # Try to write the corresponding memory address/value to commands.txt
            try:
                # Write a random colour into memory if command is "colour"
                if cmd == "colour":
                    cmd_file.write(f"{mario_commands[cmd]}{choice(colour_values)}")
                else:
                    cmd_file.write(mario_commands[cmd])

                cmd_file.write("\n")
                flash(f"Command [{cmd}] written to memory!")
                return 0
            except KeyError:
                flash(f"Command [{cmd}] not found!")
                flash("Enter 'commands' to see a list of commands.")
                return 1


    @app.route("/", methods=["GET", "POST"])
    @app.route("/index")
    def index():

        # Form object
        form = CommandForm(request.form)

        if request.method == "POST":
            command = request.form["command"].lower()
            # Perform field validation, then write command to file
            if form.validate():
                if command == "commands":
                    for cmd, help in form.commands_help.items():
                        flash(f"{cmd}: {help}")
                else:
                    CommandForm.write_command(command)
                # Redirect back to same page with empty field
                return redirect(url_for("index"))

        # Render index.html
        return render_template("index.html", form=form, url_for=url_for)


if __name__ == "__main__":
    app.run()
