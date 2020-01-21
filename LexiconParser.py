from LexicalStructures import *

class LexiconParser:
    def __init__(self):
        pass

    def parse_syntactic_category(self, cat):
        def findSlash(subcat):
            bracketcount = 0
            for i in range(len(subcat)):
                if subcat[i] == "(":
                    bracketcount += 1
                elif subcat[i] == ")":
                    bracketcount -= 1
                elif bracketcount == 0 and subcat[i] == "/":
                    return i

        if "/" not in cat:
            return SyntacticCategory(SyntacticPrimitive(cat))
        else:
            centerSlash = findSlash(cat)
            firstArg = cat[:centerSlash]
            slash = None

            if cat[centerSlash+1] == "r":
                secondArg = cat[centerSlash+2:]
                slash = SyntacticSlash.R
            elif cat[centerSlash+1] == "l":
                secondArg = cat[centerSlash+2:]
                slash = SyntacticSlash.L
            else:
                secondArg = cat[centerSlash+1:]

            if firstArg[0] == "(":
                firstArg = firstArg[1:-1]
            if secondArg[0] == "(":
                secondArg = secondArg[1:-1]
            return SyntacticCategory((self.parse_syntactic_category(firstArg), self.parse_syntactic_category(secondArg)), slash=slash)

    def parse_semantic_type(self, type):
        def findBreak(subtype):
            bracketcount = 0
            for i in range(len(subtype)):
                if subtype[i] == "<":
                    bracketcount += 1
                elif subtype[i] == ">":
                    bracketcount -= 1
                elif bracketcount == 0 and subtype[i] == ",":
                    return i

        if type[0] != "<":
            return SemanticType(SemanticPrimitive(type))
        else:
            subtype = type[1:-1]
            centerline = findBreak(subtype)
            return SemanticType((self.parse_semantic_type(subtype[:centerline]), self.parse_semantic_type(subtype[centerline+1:])))
            pass

    def parse_semantic_func(self, func):
        def tokenize(subfunc):   # This tokenizes a function: m=1 p=0 -> ["m=1", "p=0"]
            subfunc += " "
            bracketcount = 0
            start = 0
            lst = []
            i = 0
            while i < len(subfunc):
                if subfunc[i] == "(":
                    bracketcount += 1
                elif subfunc[i] == ")":
                    bracketcount -= 1
                elif bracketcount == 0 and subfunc[i] == " " or i == len(subfunc)-1:
                    lst.append(subfunc[start:i])
                    start = i+1
                    i += 1
                i += 1
            return lst

        def to_dict_entry(entry):
            if "(" not in entry:
                equals = entry.index('=')
                return {entry[:equals]: entry[equals+1:]}
            else:
                equals = entry.index('=')
                return {entry[:equals]: self.parse_semantic_func(entry[equals+2:-1])}

        tokens = tokenize(func)
        if len(tokens) == 1 and "=" not in tokens[0]:
            return SemanticFunction(tokens[0], True)
        else:
            funcDict = {}
            entries = list(map(to_dict_entry, tokens))
            for e in entries:
                funcDict.update(e)
            return SemanticFunction(funcDict)

    def parse_entry(self, entry):
        entryArray = entry.split(" ; ")
        english = entryArray[0]
        category = self.parse_syntactic_category(entryArray[1])
        type = self.parse_semantic_type(entryArray[2])
        func = self.parse_semantic_func(entryArray[3])
        entry = OpenClassEntry(type, func)
        return LexicalEntry(english, category, entry)

    def parse_file(self, filename):
        entries = []
        with open(filename, 'r') as fp:
            line = fp.readline()
            while line:
                if line[0] is not "#":
                    entries.append(self.parse_entry(line[:-1]))
                line = fp.readline()
        return entries
