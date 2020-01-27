class Lexicon:
    def __init__(self, entries):
        self.entries = entries  # A list of LexicalEntrys
        self.id_counter = 0
        self.assign_ids()

    def assign_ids(self):
        self.id_counter = 0
        for e in self.entries:
            self.assign_id(e)

    def assign_id(self, e):
        e.id = self.id_counter
        self.id_counter += 1

    def add(self, entry):
        if isinstance(entry, list):
            for e in entry:
                self.assign_id(e)
                self.entries.add(e)
        else:
            self.assign_id(entry)
            self.entries.add(entry)

    def __str__(self):
        out = "=== Lexicon ===\n"
        for e in self.entries:
            out = out + str(e) + "\n"
        return out + "==============="
