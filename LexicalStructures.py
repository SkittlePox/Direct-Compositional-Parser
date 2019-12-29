import enum
from functools import reduce

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

class SyntacticCategory:
    def __init__(self, tuple, features=None):
        self.tuple = tuple
        self.features = features

    def optional_features(self):
        if self.features is None:
            return ""
        else:
            return "["+reduce(lambda a, b: f"{a},{b}", self.features)+"]"

    def __str__(self):
        return f"({str(self.tuple[0])}\\{str(self.tuple[1])}){self.optional_features()}"

class SemanticPrimitive(enum.Enum):
    def __str__(self):
        return str(self.value)
    e = "e"
    t = "t"

class SemanticType:
    def __init__(self, tuple):
        self.tuple = tuple

    def __str__(self):
        return f"<{str(self.tuple[0])},{str(self.tuple[1])}>"
