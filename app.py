import random
import os
import requests
from flask import Flask, render_template, abort, request
from QuoteEngine import Importer
from MemeGenerator import *

app = Flask(__name__)

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
def rand_meme():
    """Generate a random Art Meme"""

    img = random.choice(images)
    quote = random.choice(quotes)

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template("meme.html", path=path)


# @app.route("/")
# def home():
#     return "Hello World!"


# @app.route("/create", methods=["GET"])
# def meme_form():
#     """ User input for meme information """
#     return render_template("meme_form.html")


# @app.route("/create", methods=["POST"])
# def meme_post():
#     """ Create a user defined meme """

#     # @TODO:
#     # 1. Use requests to save the image from the image_url
#     #    form param to a temp local file.
#     # 2. Use the meme object to generate a meme using this temp
#     #    file and the body and author form paramaters.
#     # 3. Remove the temporary saved image.

#     path = None

#     return render_template("meme.html", path=path)


if __name__ == "__main__":
    app.run()
