import random
import os
import requests
from flask import Flask, render_template, abort, request, redirect
from QuoteEngine import Importer
from MemeGenerator import *
from main import generate_meme

app = Flask(__name__)
app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0

# app.config["CACHE_TYPE"] = "null"

meme = Meme("./static")


def setup():
    """ Load all resources"""

    quote_files = [
        "./data/ArtQuotes/ArtQuotesCSV.csv",
        "./data/ArtQuotes/ArtQuotesDOC.docx",
        "./data/ArtQuotes/ArtQuotesPDF.pdf",
        "./data/ArtQuotes/ArtQuotesTXT.txt",
    ]

    quotes = []
    for file in quote_files:
        quotes.extend(Importer.parse(file))

    images_path = "./data/ArtImages"

    for root, _, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, images = setup()


@app.route("/")
def meme_rand():
    """ Generate a random Art meme """
    img = random.choice(images)
    quote = random.choice(quotes)

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


@app.route("/create", methods=["GET"])
def meme_form():
    """ User input for meme information """
    return render_template("meme_form.html")


@app.route("/create", methods=["POST"])
def meme_post():
    """ Create a user defined meme
        If user input left blank use random selection from art images and/or quotes """

    # pull image file from url if given
    image_url = request.form.get("image_url", None)
    if image_url:
        img_path = "./static/tmp_img.jpg"
        r = requests.get(image_url)
        if r.status_code == 200:
            with open(img_path, "wb") as f:
                f.write(r.content)
    else:
        img_path = None
    body = request.form.get("body", None)
    author = request.form.get("author", None)
    if body == "":
        body = None
    if author == "":
        author = None

    path = generate_meme(img_path, body, author)
    if img_path:
        os.remove(img_path)
    return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run(debug=True)
