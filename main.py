import os
import random
from MemeGenerator import *
from QuoteEngine import *
import argparse


def generate_meme(path=None, body=None, author=None):
    """Inputs:
        path: str = path to image file
        body: str = body of a quote about art
        author: str = author of an art quote

        Returns path to .jpg meme of image combined with art quote"""

    img = None
    quote = None

    if path is None:
        image_path = "./data/ArtImages"
        imgs = []
        for root, _, files in os.walk(image_path):
            imgs = [os.path.join(root, name) for name in files]
        img = random.choice(imgs)
    else:
        img = path[0]

    if body is None:
        quote_files = [
            "./data/ArtQuotes/ArtQuotesCSV.csv",
            "./data/ArtQuotes/ArtQuotesDOC.docx",
            "./data/ArtQuotes/ArtQuotesPDF.pdf",
            "./data/ArtQuotes/ArtQuotesTXT.txt",
        ]

        quotes = []
        for file in quote_files:
            quotes.extend(Importer.parse(file))

            quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception("All quotes must have an author")
        quote = QuoteModel(body, author)

    meme = Meme("./tmp")
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Create an art meme!!")
    parser.add_argument("-img_path", type=str, nargs="*")
    parser.add_argument("-body", type=str, nargs="*")
    parser.add_argument("-author", type=str, nargs="*")

    args = parser.parse_args()

    print(generate_meme(args.img_path, args.body, args.author))

