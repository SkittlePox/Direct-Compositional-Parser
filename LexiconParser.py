from LexicalStructures import *

class LexiconParser:
    def __init__(self):
        pass

    def parse_syntactic_category(self, cat):
        """
        Parses a syntactic category like S/NP or (S/NP)/(S/NP)
        """
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
        """
        Parses a semantic type like <e,t> or <e,<e,t>>
        """
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
            return SemanticType(SemanticTypePrimitive(type))
        else:
            subtype = type[1:-1]
            centerline = findBreak(subtype)
            return SemanticType((self.parse_semantic_type(subtype[:centerline]), self.parse_semantic_type(subtype[centerline+1:])))
            pass

    def parse_semantic_extension(self, func):
        """
        Parses a semantic function into a dictionary
        m=(m=1 p=1) p=(m=0 p=1) z=(m=0 p=0) -> {m: {m: 1, p: 1}, p: {m: 0, p: 1}, z: {m: 0, p: 0}}
        """
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
                return {entry[:equals]: self.parse_semantic_extension(entry[equals+2:-1])}

        tokens = tokenize(func)
        if len(tokens) == 1 and "=" not in tokens[0]:
            return tokens[0]
        else:
            funcDict = {}
            entries = list(map(to_dict_entry, tokens))
            for e in entries:
                funcDict.update(e)
            return funcDict

    def parse_semantic_intention(self, extension, english):
        """
        Assigns a name in the semantic space
        If extension is a name like 'p', it is used
        Otherwise a lowercase of english is used
        """
        if isinstance(extension.function, str):
            return SemanticIntention(argument=extension.function)
        else:
            return SemanticIntention(argument=english.lower() + "'")

    def parse_entry(self, entry):
        """
        Parses an individual lexical entry in a lexicon file
        The parsing is broken up into syntactic, semantic, etc.
        """
        entryArray = entry.split(" ; ")
        english = entryArray[0]
        category = self.parse_syntactic_category(entryArray[1])
        type = self.parse_semantic_type(entryArray[2])
        extension = SemanticExtension(self.parse_semantic_extension(entryArray[3]))
        intention = self.parse_semantic_intention(extension, english)
        entry = SemanticEntry(extension=extension, intention=intention, type=type)
        return LexicalEntry(english, category, entry)

    def parse_file(self, filename):
        """
        Turns a lexicon file into a list of LexicalEntry objects
        """
        entries = []
        with open(filename, 'r') as fp:
            line = fp.readline()
            while line:
                if line[0] is not "#":
                    entries.append(self.parse_entry(line[:-1]))
                line = fp.readline()
        return entries
