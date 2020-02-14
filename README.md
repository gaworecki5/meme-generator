meme-generator Module
    Creates a meme from artwork with quoets about art/creativity.

QuoteEngine Module
    - Parses quotes about art from multiple file types (.docx, .csv, .txt, .pdf) and 
      returns a list of QuoteModel objects
    - QuoteModel class - returns a quote with attributs .body and .author
    - All parsing encapsulated into the parse method of the Importer class
            - Importer.parse(file_path)
    - All quote files and image files saved in /data

MemeGenerator Module
    - Randomly selects an image and a quote from the files in /data and combines them into a meme with 
      a standard maximum width of 500 pixels
    - Meme class - requires an output path to save created meme
    - meme_maker method - takes input of image_path, quote.body, quote.author -> Returns file path to created
      meme in .jpg format

APP.PY
    - Flask application that allows user to create meme from random image and quote or to create their own
      meme from image url and text quote and author
    - /templates file is html templates for Flask application
    - /static file for temporary storage of images used in Flask application

MAIN.PY
    - CLI interface for meme_maker method from MemeGenerator Module
    - arguements:
        -path: str = path to image file
        -body: str = body of a quote about art
        -author: str = author of an art quote
    - arguments left blank will be randomly selected

- All dependencies listed in requirements.txt