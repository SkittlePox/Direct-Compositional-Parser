import enum

class SemanticTypePrimitive(enum.Enum):
    def __str__(self):
        return str(self.value)
    e = "e"
    t = "t"

class SemanticType:
    def __init__(self, type):
        self.primitive = isinstance(type, SemanticTypePrimitive)
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

#########################

class SemanticEntry:
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
        return f"{str(self.type)} ; {str(self.function)}"
    def __call__(self, arg):
        self.function(arg)

class ClosedClassEntry(SemanticEntry):
    def __init__(self, type, function=None):
        self.lambda_expression = lambda_expression

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

############ Experiment Below

class SemanticExpression:
    def __init__(self, function, argument_s):
        if isinstance(argument_s, list) and len(argument_s) is not 1:
            sem = function
            for arg in argument_s[:-1]:
                sem = SemanticExpression(sem, arg)
            self.baselayer = False
            self.function = sem
            self.argument = argument_s[-1]
        else:
            self.baselayer = True
            self.function = function
            self.argument = argument_s[0] if isinstance(argument_s, list) else argument_s

    def evaluate(self):
        if isinstance(self.function, dict):
            return self.function[self.argument]
        else:
            return self.function.evaluate()[self.argument]

    def __str__(self):
        return f"{str(self.function)}({str(self.argument)})"

class SemEx:
    def __init__(self, deep_function, deep_args):
        self.function = deep_function
        self.deep_args = deep_args
