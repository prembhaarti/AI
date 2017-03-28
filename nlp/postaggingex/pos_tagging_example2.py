import nltk

from nltk.tokenize import PunktSentenceTokenizer, word_tokenize

tokenized_word = word_tokenize("What are you doing? I am doing nothing")

tagged = nltk.pos_tag(tokenized_word)

for word in tagged:
    print word
