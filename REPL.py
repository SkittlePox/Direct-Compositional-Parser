from LexicalStructures import *
from Grammar import *
from LexiconParser import *
from GrammarInteractor import *
from cmd import Cmd

class REPL(Cmd):
    def __init__(self):
        self.lexicon_parser = LexiconParser()
        self.lexicon = Lexicon()
        Cmd.__init__(self)

    def do_hello(self, args):
        """Says hello. If you provide a name, it will greet you with it."""
        if len(args) == 0:
            name = 'stranger'
        else:
            name = args
        print ("Hello, %s" % name)

    def do_import(self, args):
        """Imports a lexicon."""
        if len(args) == 0:
            lex_file = "lexicon.txt"
        else:
            lex_file = args
        # self.lexicon.add(self.lexicon_parser.parse_file(lex_file))
        print("lexicon imported")


    def do_quit(self, args):
        """Quits the program."""
        raise SystemExit


if __name__ == '__main__':
    prompt = REPL()
    prompt.prompt = '> '
    prompt.cmdloop('Starting prompt...')
