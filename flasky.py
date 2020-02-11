import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import *
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

