import enum
from functools import reduce
# from SyntaxStructures import *
# from main import VERBOSE

SPACING = True
COUNTER = 0

class LexicalEntry:
    def __init__(self, english, syntacticCategory, semanticEntry):
        self.english = english
        self.category = syntacticCategory
        self.function = semanticEntry.function
        self.type = semanticEntry.type
        global COUNTER
        self.id = COUNTER
        COUNTER += 1
        
    def __eq__(self, other):
        return isinstance(other, LexicalEntry) \
        and self.english == other.english and self.category == other.category \
        and self.type == other.type #and self.function == other.function
    def __str__(self):
        cat = str(self.category)
        # if not self.category.primitive:
        #     cat = cat[1:-1]
        if SPACING:
            return f"<[{self.id}] \"{self.english}\" ; {cat} ; {str(self.type)} ; {str(self.function)} >"
        return f"<\"{self.english}\";{cat};{str(self.type)};{str(self.function)}>"
    def __hash__(self):
        return hash(self.english) # LOL easy way out
