from __future__ import unicode_literals
from __future__ import print_function
import sys
import plac
import bz2
import ujson
import spacy.en
def main(input_loc):
    nlp = spacy.en.English()                 # Load the model takes 10-20 seconds.
    for line in bz2.BZ2File(input_loc):      # Iterate over the Reddit comments from the dump.
        comment_str = ujson.loads(line)['body']  # Parse the json object, and extract the 'body' attribute.


def google_doing_something(w):
    if w.lower_ != 'google':
        return False
    # Is it the subject of a verb?
    elif w.dep_ != 'nsubj':
        return False
    # And not 'is'
    elif w.head.lemma_ == 'be' and w.head.dep_ != 'aux':
        return False
    # Exclude e.g. "Google says..."
    elif w.head.lemma_ in ('say', 'show'):
        return False
    else:
        return True

if __name__ == '__main__':
    plac.call(main)


comment_parse = nlp(comment_str)
for word in comment_parse:
    if google_doing_something(word):
        # Print the clause
        print(''.join(w.string for w in word.head.subtree).strip())
