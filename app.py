from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey"

debug = DebugToolbarExtension(app)

@app.route("/")
def show_form():
    """renders the main page with madlib form"""

    prompts = story.prompts

    return render_template("base.html", prompts = prompts )


@app.route("/story")
def show_story():
    """Takes answers from submitted form on homepage and plugs them into story template and displays on page"""
    print(story)
    ans = request.args
    mad_story = story.generate(ans)
    return render_template("story.html", story=mad_story)