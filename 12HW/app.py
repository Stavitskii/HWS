from flask import Flask, Blueprint, request, render_template, send_from_directory
from main.main import main_blueprint
from loader.loader import loader_blueprint
from main.utils import *


POST_PATH = "posts.json"
UPLOAD_FOLDER = "uploads/images"

app = Flask(__name__)


app.register_blueprint(main_blueprint)
app.register_blueprint(loader_blueprint)

if __name__ == "__main__":
    app.run()

