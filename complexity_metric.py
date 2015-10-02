
# Set up spaCy
from scipy.stats import norm
from spacy.en import English
import sys
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

# parser = English()
pipeline = English()

length_normalized_complexity = []
with open('./WSJ/wsj.flat') as f:
    for line in f:
        tokens = pipeline(line)
        headAndToken = [(token.idx,token.head.idx) for ind, token in enumerate(tokens)]
        totalScore = sum([abs(tokenIndex-tokenHeadIndex) for tokenIndex,tokenHeadIndex in headAndToken])
        totalScore = totalScore/len(tokens)
        length_normalized_complexity.append(totalScore)

#plt.plot(range(len(length_normalized_complexity)),length_normalized_complexity)
n, bins, patches = plt.hist(length_normalized_complexity,bins=200, normed=1, facecolor='green', alpha=0.75)
(mu, sigma) = norm.fit(length_normalized_complexity)
y = mlab.normpdf( bins, mu, sigma)
l = plt.plot(bins, y, 'r--', linewidth=2)
plt.xlabel('Smarts')
plt.ylabel('Probability')
plt.title(r'$\mathrm{Histogram\ of\ IQ:}\ \mu=%.3f,\ \sigma=%.3f$' %(mu, sigma))
plt.grid(True)
plt.show()

# print("Complexity Score:",total_score)

# [-1, 2, 0, 0, 3, 0, 7, 5, 7, 10, 8, 0, 13, 15, 15, 11]
# for i, h in enumerate(parsedData):
#     head = tokens[parsedData[h]] if h >= 1 else 'None'
# print(tokens[i] + ' <-- ' + head)
