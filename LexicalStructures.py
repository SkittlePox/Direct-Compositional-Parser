import enum
from functools import reduce
# from main import VERBOSE

VERBOSE = True

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
        return self.value
    A = "A"
    V = "V"

class SyntacticSlash(enum.Enum):
    def __str__(self):
        if VERBOSE:
            return self.value
        else:
            return ""
    L = "˻"
    R = "ʳ"

class SyntacticCategory:
    # def __init__(self, cat, slash=None, features=None):
    #     self.primitive = isinstance(cat, SyntacticPrimitive)
    #     if self.primitive:
    #         self.lhs = cat
    #         self.rhs = None
    #     else:
    #         self.lhs = cat[0]
    #         self.rhs = cat[1]
    #
    #     self.features = features
    #     if slash == None and self.primitive == False:
    #         if self.lhs.primitive and self.lhs.lhs == SyntacticPrimitive.S:
    #             self.slash = SyntacticSlash.L
    #         elif self.lhs == self.rhs:
    #             self.slash = SyntacticSlash.L
    #         else:
    #             self.slash = SyntacticSlash.R
    #     else:
    #         self.slash = slash

    def __init__(self, cat, slash=None, features=None):
        self.primitive = isinstance(cat, SyntacticPrimitive)
        if self.primitive:
            self.lhs = cat
            self.rhs = None
        else:
            self.lhs = cat[0]
            self.rhs = cat[1]

        self.features = features
        if slash == None and self.primitive == False:
            if self.lhs.primitive and self.lhs.lhs == SyntacticPrimitive.S:
                self.slash = SyntacticSlash.L
            elif self.lhs == self.rhs:
                self.slash = SyntacticSlash.L
            else:
                self.slash = SyntacticSlash.R
        else:
            self.slash = slash

    def optional_features(self):
        if self.features is None:
            return ""
        else:
            return "["+reduce(lambda a, b: f"{a},{b}", self.features)+"]"

    def possible_primitive(self):
        if self.primitive:
            return f"{str(self.lhs)}"
        else:
            return f"({str(self.lhs)}/{str(self.slash)}{str(self.rhs)})"

    def __str__(self):
        return f"{self.possible_primitive()}{self.optional_features()}"

    def __eq__(self, other):
        return isinstance(other, SyntacticCategory) \
        and self.lhs == other.lhs and self.rhs == other.rhs \
        and self.features == other.features and self.slash == other.slash

#### Semantics

class SemanticPrimitive(enum.Enum):
    def __str__(self):
        return str(self.value)
    e = "e"
    t = "t"

class SemanticType:
    def __init__(self, type):
        self.primitive = isinstance(type, SemanticPrimitive)
        if self.primitive:
            self.lhs = type
            self.rhs = None
        else:
            self.lhs = type[0]
            self.rhs = type[1]

    def __str__(self):
        if self.primitive:
            return str(self.lhs)
        else:
            return f"<{str(self.lhs)},{str(self.rhs)}>"

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
