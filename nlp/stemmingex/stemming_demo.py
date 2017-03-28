from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize

ps = PorterStemmer()

example = ["python","pythoner","pythoning","pythoned","pythonly"]

# first tokenizing the sentence into words
example2 = word_tokenize("It is important to by very pythonly while you are pythoning with python. All pythoners have pythoned poorly at least once.")

print example2

for word in example:
    print (ps.stem(word))

for word2 in example2:
    print (ps.stem(word2))