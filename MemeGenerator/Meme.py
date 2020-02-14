from PIL import Image, ImageDraw, ImageFont
import textwrap
import random


class Meme:
    """Class to create a meme given an image file path and Quote"""

    def __init__(self, out_path: str):
        self.out_path = out_path

    def make_meme(self, img_path, text, author, width=500):
        """Method to take input image path and quote and combines them randomly to create a meme"""

        img = Image.open(img_path)
        scale_ratio = width / float(img.width)
        new_height = int(scale_ratio * float(img.height))
        img = img.resize((width, new_height), Image.NEAREST)

        # Add quote to the image
        d = ImageDraw.Draw(img)
        if img.width / float(img.height) <= 0.75:
            text_size = 35
            location = random.randint(1, 7) / float(10)
        else:
            text_size = 20
            location = random.randint(1, 3) / float(5)
        font_text = ImageFont.truetype(
            "./data/fonts/DancingScript-Medium.ttf", text_size
        )
        font_author = ImageFont.truetype(
            "./data/fonts/Hind-Regular.ttf", text_size - 10
        )

        text_size = font_text.getsize(text)
        text_ratio = text_size[0] / float(width - 20)
        line_length = int(len(text) / text_ratio)
        num_lines = len(textwrap.wrap(text, line_length))
        text = textwrap.fill(text, line_length)

        # draw text and author onto image
        d = ImageDraw.Draw(img)
        d.text((10, location * img.height), text, fill="black", font=font_text)
        author_location = (
            int(img.width / 4),
            location * img.height + text_size[1] * num_lines,
        )
        d.text(author_location, author, fill="black", font=font_author)

        # save and return the path to created meme
        meme_path = f"{self.out_path}/temp_meme_.jpg"
        img.save(meme_path)
        return meme_path

