class Lexicon:
    def __init__(self, entries):
        self.entries = entries

    def add(self, entry):
        if isinstance(entry, list):
            for e in entry:
                self.entries.add(e)
            # map(lambda e: self.entries.add(e), entry)
            # self.entries.extend(entry)
        else:
            self.entries.add(entry)


    def __str__(self):
        out = "=== Lexicon ===\n"
        for e in self.entries:
            out = out + str(e) + "\n"
        return out + "==============="
