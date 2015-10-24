
# Set up spaCy
from scipy.stats import norm
from spacy.en import English
import sys
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from readability.readability import Readability


# parser = English()
pipeline = English()

length_normalized_complexity = []
FKGradeLevel = []
with open('./WSJ/wsj.flat') as f:
    for line in f:
        tokens = pipeline(line)
        headAndToken = [(token.idx,token.head.idx) for ind, token in enumerate(tokens)]
        totalScore = sum([abs(tokenIndex-tokenHeadIndex) for tokenIndex,tokenHeadIndex in headAndToken])
        totalScore = totalScore/len(line)
        length_normalized_complexity.append(totalScore)
        FKGradeLevel.append(Readability(line).FleschReadingEase())


highestComplexity = max(length_normalized_complexity)
length_normalized_complexity = [complexity*100/highestComplexity for complexity in length_normalized_complexity]
#plt.plot(range(len(length_normalized_complexity)),length_normalized_complexity)
n, bins, patches = plt.hist(length_normalized_complexity,bins=200, normed=1, facecolor='green', alpha=0.50)
n2,bins2, patches2 = plt.hist(FKGradeLevel,bins=200, normed=1, facecolor='red', alpha=0.50)
(mu, sigma) = norm.fit(length_normalized_complexity)
y = mlab.normpdf( bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=2)
plt.xlabel('Length between Dependancies')
plt.ylabel('number of sentences in corpus')
plt.title(r'$\mathrm{Histogram\ of\ Normalised Dependancy Lengths:}\ \mu=%.3f,\ \sigma=%.3f$' %(mu, sigma))
plt.grid(True)
plt.show()

# print("Complexity Score:",total_score)

# [-1, 2, 0, 0, 3, 0, 7, 5, 7, 10, 8, 0, 13, 15, 15, 11]
# for i, h in enumerate(parsedData):
#     head = tokens[parsedData[h]] if h >= 1 else 'None'
# print(tokens[i] + ' <-- ' + head)
