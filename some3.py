import nltk
from nltk.grammar import DependencyGrammar
from nltk.parse import (
DependencyGraph,
ProjectiveDependencyParser,
NonprojectiveDependencyParser,
)
groucho_dep_grammar = nltk.DependencyGrammar.fromstring("""
'shot' -> 'I' | 'elephant' | 'in'
'elephant' -> 'an' | 'in'
'in' -> 'pajamas'
'pajamas' -> 'my'
""")
print(groucho_dep_grammar)
pdp = nltk.ProjectiveDependencyParser(groucho_dep_grammar)
sent = 'I shot an elephant in my pajamas'.split()
trees = pdp.parse(sent)
if len(str(trees))>1:
    print("Your sentence has more than one interpretations!")

for tree in trees:
    n_trailing_brackets = 0
    while str(tree)[len(str(tree))-1-n_trailing_brackets]==")":
        n_trailing_brackets+=1
    print("The height of your parse tree is",n_trailing_brackets)
    print(tree)
