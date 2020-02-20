class Individual:
    def __init__(self, english):
        self.type = SemanticType(rhs=SemanticTypePrimitive.e)
        self.english = english
        self.function_map = {}

    def __call__(self, function_name, argument):
        if function_name in self.function_map.keys():
            return self.function_map[function_name](argument)
