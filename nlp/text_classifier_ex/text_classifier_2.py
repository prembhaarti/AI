import  nltk
from nltk.corpus import movie_reviews

all_movie_words = movie_reviews.words()

top_common_words = list(nltk.FreqDist(all_movie_words).keys())[:10]
# top_common_words = nltk.FreqDist(all_movie_words).most_common(3000)

# custom_top_common_words =

print top_common_words
