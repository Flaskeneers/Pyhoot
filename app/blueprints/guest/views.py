from flask import render_template

from . import bp_guest


@bp_guest.get("/")
def index():
    return render_template("guest/index.html")
