import enum

VERBOSE = True

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
