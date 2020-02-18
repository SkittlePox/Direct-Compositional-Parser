import enum

class SemanticTypePrimitive(enum.Enum):
    def __str__(self):
        return str(self.value)
    e = "e"
    t = "t"

class SemanticType:
    def __init__(self, lhs=None, rhs=None):
        self.lhs = lhs
        self.rhs = rhs

    def complexity(self):
        if self.lhs == None:
            return 1
        lhs = 1 if isinstance(self.lhs, SemanticTypePrimitive) else self.lhs.complexity()
        rhs = 1 if isinstance(self.rhs, SemanticTypePrimitive) else self.rhs.complexity()
        return lhs + rhs

    def __call__(self, argument):
        return self.rhs

    def __str__(self):
        if self.lhs == None:
            return str(self.rhs)
        else:
            return f"<{str(self.lhs)},{str(self.rhs)}>"

    def __eq__(self, other):
        return isinstance(other, SemanticType) \
        and self.lhs == other.lhs and self.rhs == other.rhs

#########################

# class SemanticFunction:
#     def __init__(self, function):
#         def get_dict_function(dictionary):
#             def func(x):
#                 if x in dictionary:
#                     return SemanticExtensionDict(function=dictionary[x])
#                 else:
#                     return SemanticExtensionDict(function={})
#             return func
#
#         if isinstance(function, dict):
#             self.function = get_dict_function(function)

# class SemanticFunction:
#     def __init__(self, function):
#         self.dictionary = None
#         self.function
#
# class SemTest:
#     def __init__(self, var):
#         def give_var(seb):
#             return var
#
#         self.var = var


class SemanticExtension:
    pass

class SemanticExtensionLambda(SemanticExtension):
    def __init__(self, function):
        """
        function is an actual function made from a class of functions
        """
        self.function = function

    def __call__(self, argument):
        return self.function(argument)

class SemanticExtensionDict(SemanticExtension):
    def __init__(self, function):
        """
        function is a dictionary like {m: 1, p: 1}, maybe it should be an actual function that wraps a dictionary
        """
        self.function = function

    def update(self, new_entries):
        def dict_updater(orig_dict, entries):
            for key, val in entries.items():
                if isinstance(val, dict):
                    dict_updater(orig_dict[key], val)
                else:
                    orig_dict.update({key: val})
        dict_updater(self.function, new_entries)

    def __call__(self, argument):
        if argument.function in self.function:
            return SemanticExtensionDict(function=self.function[argument.function])
        else:
            return SemanticExtensionDict(function={})

    def __str__(self):
        def dict_to_special(dictionary):
            baseStr = ""
            for key, value in dictionary.items():
                if isinstance(value, str):
                    baseStr += f"{key}={str(value)} "
                else:
                    baseStr += f"{key}=({dict_to_special(value)}) "
            baseStr = baseStr[:-1]
            return baseStr

        if isinstance(self.function, str) or isinstance(self.function, int):
            return str(self.function)
        elif not self.function:
            return "undefined"
        else:
            return dict_to_special(self.function)

#########################


class SemanticIntention:
    def __init__(self, function=None, argument=None):
        """
        Takes a function and argument

        function: This might look like 'likes(a)'
        argument: This might look like 'b'

        Together this intention would represent 'likes(a)(b)'

        In the case of a primitive like 'charlie'
        function = None (This should probably be some identity function)
        argument = 'charlie'
        """
        self.function = function
        self.argument = argument

    def __call__(self, argument):
        return SemanticIntention(function=self, argument=argument)

    def __str__(self):
        if self.function is None:
            return str(self.argument)
        else:
            return f"{str(self.function)}({str(self.argument)})"

#########################

class SemanticEntry:
    def __init__(self, intention=None, extension=None, type=None):
        """
        Takes a SemanticIntention, SemanticExtension, and SemanticType
        """
        self.intention = intention
        self.extension = extension
        self.type = type

    def update(self, new_entries):
        self.extension.update(new_entries)

    def complexity(self):
        return self.type.complexity()

    def __call__(self, argument):
        """
        argument is another SemanticEntry
        """
        intention = self.intention(argument.intention)
        extension = self.extension(argument.extension)
        type = self.type(argument.type)
        return SemanticEntry(intention=intention, extension=extension, type=type)

    def __str__(self):
        baseStr = ""
        baseStr += str(self.type)
        baseStr += " ; "
        baseStr += str(self.intention)
        baseStr += " ; "
        baseStr += str(self.extension)
        return baseStr
