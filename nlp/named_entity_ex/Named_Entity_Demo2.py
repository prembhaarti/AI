import nltk

from nltk import word_tokenize

# example= "White house is very good and White guy was rude."
example= "Prem Bharti was very rude"

tokenized= word_tokenize(example)
tagged = nltk.pos_tag(tokenized)

namedEntity=nltk.ne_chunk(tagged,binary=False)

namedEntity.draw()
