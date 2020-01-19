import enum
from functools import reduce
# from main import VERBOSE

VERBOSE = True
SPACING = True

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

    def __eq__(self, other):
        return isinstance(other, SemanticType) \
        and self.primitive == other.primitive \
        and self.lhs == other.lhs and self.rhs == other.rhs

class SemanticFunction:
    def __init__(self, func, primitive=False):
        self.func = func
        self.primitive = primitive

    def __call__(self, arg):
        if arg.func in self.func:
            return self.func[arg.func]
        else:
            return SemanticFunctionUnknown()

    def __str__(self):
        if self.primitive:
            return self.func
        else:
            baseStr = ""
            for key, value in self.func.items():
                if isinstance(value, str):
                    baseStr += f"{key}={str(value)} "
                else:
                    baseStr += f"{key}=({str(value)}) "
            baseStr = baseStr[:-1]
            return baseStr

class SemanticFunctionUnknown(SemanticFunction):
    def __init__(self):
        self.primitive = True
        self.func = "UND"
        pass
    def __call__(self, arg):
        return SemanticFunctionUnknown()

class SemanticEntry:
    # A function is just a dictionary! Function of function is a dictionary of dictionaries!
    def __init__(self, type):
        self.type = type
        pass
    # def __call__(self, ):
    #     pass

class OpenClassEntry(SemanticEntry):
    def __init__(self, type, function=None):
        self.type = type
        self.function = function
    def __str__(self):
        return str(self.type)
    def __call__(self, arg):
        self.function(arg)

# class ClosedClassEntry(SemanticEntry):
#     def __init__(self, lambda_expression):
#         self.lambda_expression = lambda_expression


#### Lexical Entry

class LexicalEntry:
    def __init__(self, english, syntacticCategory, semanticEntry):
        self.english = english
        self.category = syntacticCategory
        self.function = semanticEntry.function
        self.type = semanticEntry.type
    def __eq__(self, other):
        return isinstance(other, LexicalEntry) \
        and self.english == other.english and self.category == other.category \
        and self.type == other.type #and self.function == other.function
    def __str__(self):
        cat = str(self.category)
        # if not self.category.primitive:
        #     cat = cat[1:-1]
        if SPACING:
            return f"< \"{self.english}\" ; {cat} ; {str(self.type)} ; {str(self.function)} >"
        return f"<\"{self.english}\";{cat};{str(self.type)};{str(self.function)}>"
    def __hash__(self):
        return hash(self.english) # LOL easy way out
