from flask import Blueprint, render_template, request
from main.utils import *
import logging
from exceptions import *

logging.basicConfig(filename="logger.log", level=logging.INFO)


main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')
@main_blueprint.route('/')
def main_page():
    logging.info("Открытие главной страницы")
    return render_template("index.html")


@main_blueprint.route("/search")
def search_page():
    logging.info("Выполняется поиск")
    s = request.args.get("s", "")
    try:
        posts = get_post_by_substring('posts.json',s)
    except DataJsonError:
        return "Posts file loading error"

    return render_template("post_list.html", posts=posts, s=s)


