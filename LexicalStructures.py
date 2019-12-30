import enum
from functools import reduce

#### Syntax

class SyntacticPrimitive(enum.Enum):
    def __str__(self):
        return str(self.value)
    S = "S"
    NP = "NP"
    PP = "PP"
    N = "N"
    CP = "CP"

class SyntacticFeature(enum.Enum):
    def __str__(self):
        return str(self.value)
    A = "A"
    V = "V"

class SyntacticSlash(enum.Enum):
    def __str__(self):
        if self == SyntacticSlash.L:
            return ""
        else:
            return self.value
    L = "˻"
    R = "ʳ"

class SyntacticCategory:
    def __init__(self, cat, slash=SyntacticSlash.L, features=None):
        if isinstance(cat, SyntacticPrimitive):
            self.tuple = (cat, None)
        else:
            self.tuple = cat
        self.features = features
        self.slash = slash

    def optional_features(self):
        if self.features is None:
            return ""
        else:
            return "["+reduce(lambda a, b: f"{a},{b}", self.features)+"]"

    def possible_primitive(self):
        if self.tuple[1] == None:
            return str(self.tuple[0])
        else:
            return f"({str(self.tuple[0])}/{str(self.slash)}{str(self.tuple[1])})"

    def __str__(self):
        return f"{self.possible_primitive()}{self.optional_features()}"

#### Semantics

class SemanticPrimitive(enum.Enum):
    def __str__(self):
        return str(self.value)
    e = "e"
    t = "t"

class SemanticType:
    def __init__(self, type):
        self.primitive = isinstance(type, SemanticPrimitive)
        self.tuple = type

    def __str__(self):
        if self.primitive:
            return str(self.tuple)
        else:
            return f"<{str(self.tuple[0])},{str(self.tuple[1])}>"

class SemanticEntry:
    def __init__(self):
        pass

class OpenClassEntry(SemanticEntry):
    def __init__(self, expression):
        self.expression = expression

    def __str__(self):
        return self.expression

# class ClosedClassEntry(SemanticEntry):
#     def __init__(self, lambda_expression):
#         self.lambda_expression = lambda_expression


#### Entry

class LexicalEntry:
    def __init__(self, english, syntacticCategory, semanticType):
        self.english = english
        self.category = syntacticCategory
        self.type = semanticType
    def __str__(self):
        return f"< \"{self.english}\" ; {str(self.category)} ; {str(self.type)} >"
