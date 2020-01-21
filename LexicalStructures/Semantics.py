import enum

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
        self.func = func    # This is just a dictionary
        self.primitive = primitive
        # if self.primitive:
        #     self.name = func
        # else:

    def __call__(self, arg):
        # Change this so that the entire function is stored, not just the result
        # Also cache the latest result
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
        # self.arg = arg
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

class ClosedClassEntry(SemanticEntry):
    def __init__(self, type, function=None):
        self.lambda_expression = lambda_expression
