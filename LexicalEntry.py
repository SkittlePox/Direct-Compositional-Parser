class LexicalEntry:
    def __init__(self, eng, syntacticCategory, semanticType):
        self.eng = eng
        self.category = syntacticCategory
        self.type = semanticType
    def __str__(self):
        return f"< \"{self.eng}\" ; {str(self.category)} ; {str(self.type)} >"
