# Direct-Compositional-Parser

This is an implementation of the Direct Compositional semantic framework as given in CLPS 1342: Compositional Semantics

Add entries to lexicon.txt following the patter and run main.py. Parsing rules are not perfectly enforced. If you abuse them, it just wont work.

```
Zinkly ; NP ; e ; z
walks ; S/NP ; <e,t> ; m=1 p=0 z=0
< "Zinkly walks" ; S ; t ; 0 >
```

 This framework has support for custom grammar rules by writing a `test()` and `operate()` function:

```python
 class CombinatoryRule():   
  	def __init__(self, name, test, operate):
        """
        test takes syntactic grammar categories
        Returns whether or not this rule can operate on the given categories

        operate takes whole lexical entries
        Returns the resulting lexical entry after applying this rule
        """
        self.name = name
        self.test = test
        self.operate = operate

    def __call__(self, a, b):
        return self.operate(a, b)

    def __str__(self):
        return self.name
```



Example rule:

```python
### R-1a

def R1a_test(a, b):
    return a.slash == SyntacticSlash.R and a.rhs == b

def R1a_operate(a, b):
    newName = f"{a.english} {b.english}"
    newCat = a.category.lhs
    newEnt = a.function(b.function)
    newSem = OpenClassEntry(a.type.rhs, newEnt)
    return LexicalEntry(newName, newCat, newSem)
```

