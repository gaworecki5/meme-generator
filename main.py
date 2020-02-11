import os
import random
from MemeGenerator import *
from QuoteEngine import Importer, QuoteModel
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
        path = "./data/ArtImages"
        imgs = []
        for root, _, files in os.walk(path):
            imgs = [os.path.join(root, name) for name in files]
        img = random.choice(imgs)
    else:
        img = path

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
    meme_path = meme.make_meme(img, quote.body, quote.author)
    return meme_path


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Create an art meme!!")
    parser.add_argument("-img_path", type=str, default=None)
    parser.add_argument("-body", type=str, default=None)
    parser.add_argument("-author", type=str, default=None)

    args = parser.parse_args()

    # print(args.img_path, type(args.img_path))
    # print(args.body, type(args.body))
    # print(args.author, type(args.author))
    print(generate_meme(args.img_path, args.body, args.author))

    # generate_meme(
    #     "C:\\Users\\agaworecki\\Downloads\\taft_test1.jpg",
    #     body="some Quote about really thoughtful stuff",
    #     author="smart person",
    # )
