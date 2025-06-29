from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/user/<username>")
def show_user_profile(username):
    # Show the user profile for that user
    return f"User {escape(username)}"


@app.route("/post/<int:post_id>")
def show_post(post_id):
    # Show the post with the given id, the id is an integer
    return f"Post {post_id}"


@app.route("/path/<path:subpath>")
def show_subpath(subpath):
    # Show the subpath after /path/
    return f"Subpath {escape(subpath)}"
