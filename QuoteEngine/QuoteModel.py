class QuoteModel:
    """ Class blah blah"""

    def __init__(self, body: str, author: str):
        self.body = body
        self.author = author

    def __repr__(self):
        return f'"{self.body}" - {self.author}'

    if __name__ == "__main__":
        q1 = QuoteModel("something special", "author D")
        print(q1.body)
