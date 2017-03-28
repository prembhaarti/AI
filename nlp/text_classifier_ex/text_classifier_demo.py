import nltk
import random
from nltk.corpus import movie_reviews

# documents = [(list(movie_reviews.words(fileid)), category)
#              for category in movie_reviews.categories()
#              for fileid in movie_reviews.fileids(category)]

documents = []

# take each category of movies
# take each file id from current category
# take each word from current fileId
# append in the document

# here we're giving fileIds from where words will be loaded

for category in movie_reviews.categories():
    for fileid in movie_reviews.fileids(category):
        documents.append(list(movie_reviews.words(fileid)))

random.shuffle(documents)

# print(documents[2])

#
all_words = []

# getting all words from all movie reviews
for w in movie_reviews.words():
    all_words.append(w.lower())

print "Total words:", len(all_words)

all_words = nltk.FreqDist(all_words)

# gives most common words in all movie reviews
# print(all_words.most_common(10))
print all_words[:10]
# internally it keeps all words in dictionary in keys as word and values as their frequencies
# print all_words.viewkeys()
# print all_words.viewvalues()

# all_words is as dictionary, so we can get value by key
print(all_words["stupid"])