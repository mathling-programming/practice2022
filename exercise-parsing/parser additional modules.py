from nlparse import *


class StarParser(Parser):
    """Parser that calls the underlying parser zero or more times, concatenating the resulting constituents."""

    def __init__(self, p):
        self.p = p

    def __call__(self, tokens):
        yield (Constituent(), tokens)
        for c, tokens1 in self.p(tokens):
            for c2, tokens2 in self(tokens1):
                yield (c + c2, tokens2)
