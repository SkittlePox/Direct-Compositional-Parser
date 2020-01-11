from LexicalStructures import *

class LexiconParser:
    def __init__(self):
        pass

    def parseSyntacticCategory(self, cat):
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
            secondArg = cat[centerSlash+1:]

            if firstArg[0] == "(":
                firstArg = firstArg[1:-1]
            if secondArg[0] == "(":
                secondArg = secondArg[1:-1]
            return SyntacticCategory((self.parseSyntacticCategory(firstArg), self.parseSyntacticCategory(secondArg)))

    def parseSemanticType(self, type):
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
            return SemanticType((self.parseSemanticType(subtype[:centerline]), self.parseSemanticType(subtype[centerline+1:])))
            pass

    def parseEntry(self, entry):
        entryArray = entry.split(" ; ")
        english = entryArray[0]
        category = self.parseSyntacticCategory(entryArray[1])
        type = self.parseSemanticType(entryArray[2])
        return LexicalEntry(english, category, type)

    def parseFile(self, filename):
        entries = []
        with open(filename, 'r') as fp:
            line = fp.readline()
            while line:
                entries.append(self.parseEntry(line[:-1]))
                line = fp.readline()
        return entries
