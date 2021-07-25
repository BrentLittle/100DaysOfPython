from flask import Flask, render_template
from post import Post
import requests

posts = requests.get("https://api.npoint.io/ed99320662742443cc5b").json()
postObjects = []
for post in posts:
    postObj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    postObjects.append(postObj)

app = Flask(__name__)


@app.route('/')
def getAllPosts():
    return render_template("index.html", all_posts=postObjects)


@app.route("/post/<int:index>")
def showPost(index):
    requestedPost = None
    for blogPost in postObjects:
        if blogPost.id == index:
            requestedPost = blogPost
    return render_template("post.html", post=requestedPost)


if __name__ == "__main__":
    app.run(debug=True)


