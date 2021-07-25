from flask import Flask, render_template
import random, datetime, requests

app = Flask(__name__)


@app.route("/")
def home():
    randNum = random.randint(1,10)
    year = datetime.datetime.now().year
    return render_template("index.html", randNum = randNum, year = year)


@app.route("/guess/<name>")
def nameAgeGenderPage(name):
    nameParam = {
        "name": name,
    }

    genderResponse = requests.get(url="https://api.genderize.io", params = nameParam)
    gender = genderResponse.json()["gender"]

    ageResponse = requests.get(url="https://api.agify.io", params = nameParam)
    age = ageResponse.json()["age"]

    return render_template("customName.html", name = name, gender = gender, age = age)


@app.route("/blog/<num>")
def blogPage(num):
    print(num)
    blogURL = "https://api.npoint.io/ed99320662742443cc5b"
    response = requests.get(blogURL)
    posts = response.json()
    return render_template("blog.html", posts = posts)



if __name__ == "__main__":
    app.run()