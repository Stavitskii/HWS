from flask import Flask, render_template
import utils

app = Flask(__name__)


@app.route("/")
def list_candidates():
    candidates = utils.load_candidates_from_json("candidates.json")
    return render_template("list.html", candidates=candidates)


app.run()
