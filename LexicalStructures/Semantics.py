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

    def __call__(self, argument):
        return self.rhs

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
    def __init__(self, intention=None, extension=None, type=None):
        """
        Takes a SemanticIntention, SemanticExtension, and SemanticType
        """
        self.intention = intention
        self.extension = extension
        self.type = type

    def update(self, new_entries):
        self.extension.update(new_entries)

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

class SemanticExtension:
    def __init__(self, function):
        """
        function is a dictionary like {m: 1, p: 1}
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
            return SemanticExtension(function=self.function[argument.function])
        else:
            return SemanticExtension(function={})

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
