from flask import Blueprint, render_template, request
import utils

import logging


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='../templates')
@main_blueprint.route('/')
def main_page():
    return render_template("index.html")

@main_blueprint.route("/search")
def search_page():
    s = request.args.get("s")
    posts = utils.get_post_by_substrind(s, "../posts.json")
    return render_template("post_list.html", posts=posts, s=s)


