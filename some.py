import spacy.en
from spacy.parts_of_speech import ADV
nlp = spacy.en.English()
# Find log probability of Nth most frequent word
probs = [lex.prob for lex in nlp.vocab]
probs.sort()
is_adverb = lambda tok: tok.pos == ADV and tok.prob < probs[-1000]
tokens = nlp(u"‘Give it back,’ he pleaded abjectly, ‘it’s mine.’")
print(u''.join(tok.string.upper() if is_adverb(tok) else tok.string for tok in tokens))
pleaded = tokens[7]
print(pleaded.vector.shape)
print(pleaded.vector[:5])
from numpy import dot
from numpy.linalg import norm
cosine = lambda v1, v2: dot(v1, v2) / (norm(v1) * norm(v2))
words = [w for w in nlp.vocab if w.has_vector]
words.sort(key=lambda w: cosine(w.vector, pleaded.vector))
words.reverse()
print('1-20', ', '.join(w.orth_ for w in words[0:20]))
print('50-60', ', '.join(w.orth_ for w in words[50:60]))
print('100-110', ', '.join(w.orth_ for w in words[100:110]))
print('1000-1010', ', '.join(w.orth_ for w in words[1000:1010]))
print('50000-50010', ', '.join(w.orth_ for w in words[50000:50010]))
say_verbs = ['pleaded', 'confessed', 'remonstrated', 'begged', 'bragged', 'confided', 'requested']
say_vector = sum(nlp.vocab[verb].vector for verb in say_verbs) / len(say_verbs)
words.sort(key=lambda w: cosine(w.vector,say_vector))
words.reverse()
print('1-20', ', '.join(w.orth_ for w in words[0:20]))
print('50-60', ', '.join(w.orth_ for w in words[50:60]))
print('1000-1010', ', '.join(w.orth_ for w in words[1000:1010]))
