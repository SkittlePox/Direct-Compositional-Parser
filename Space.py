from LexicalStructures import *
from Grammar import *
from LexiconParser import *
from GrammarInteractor import *

class Space():
    self.lexicon_parser = LexiconParser()
    self.lexicon = Lexicon()

    def import_lexicon(self, args):
        if len(args) == 0:
            lex_file = "lexicon.txt"
        else:
            lex_file = args
        self.lexicon.add(self.lexicon_parser.parse_file(lex_file))

        
