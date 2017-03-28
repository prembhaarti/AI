# import nltk

# nltk.internals.config_java("/usr/lib/jvm/java-8-oracle/bin/java")
# nltk.data.path.append("/home/prembharti/nltk_data/")

from nltk.tokenize import sent_tokenize, word_tokenize

TEXT = "Hello Mr. Smith, how are you doing today? The weather is great, and Python is awesome. The sky is pinkish-blue. You shouldn't eat cardboard."

tokenized_sentence=sent_tokenize(TEXT)
tokenized_words=word_tokenize(TEXT)

print tokenized_sentence
print tokenized_words

