from app import app, db
from flask import render_template, request, redirect
from models import Link
from auth import auth


@app.route("/<short_url>")
def redirect_to_url(short_url):
    link = Link.query.filter_by(short_url=short_url).first_or_404()

    link.visits += 1
    db.session.commit()

    return redirect(link.original_url)


@app.route("/")
@auth.login_required
def index():
    return render_template("index.htm")


@app.route("/add_link", methods=["POST"])
@auth.login_required
def add_link():
    original_url = request.form["original_url"]
    link = Link(original_url=original_url)
    db.session.add(link)
    db.session.commit()

    return render_template("link_added.htm",
        new_link=link.short_url, original_url=link.original_url)


@app.route("/stats")
@auth.login_required
def stats():
    links = Link.query.all()

    return render_template("stats.htm", links=links)


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.htm"), 404


@app.errorhandler(403)
def forbidden(e):
    # note that we set the 403 status explicitly
    return render_template('403.htm'), 403


@app.errorhandler(410)
def not_good(e):
    # note that we set the 410 status explicitly
    return render_template('410.htm'), 410


@app.errorhandler(500)
def internal_server(e):
    # note that we set the 500 status explicitly
    return render_template('500.htm'), 500
