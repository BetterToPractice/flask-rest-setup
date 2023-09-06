from flask import redirect


def home_view():
    return redirect("/docs")
