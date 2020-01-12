class Lexicon:
    def __init__(self, entries):
        self.entries = entries

    def __str__(self):
        out = "=== Lexicon ===\n"
        for e in self.entries:
            out = out + str(e) + "\n"
        return out + "==============="
