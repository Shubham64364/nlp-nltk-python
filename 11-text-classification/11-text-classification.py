# 11-text-classification.py
"""
Text Classification with NLTK
-----------------------------
This script demonstrates the basics of **text classification** using the
Movie Reviews corpus in NLTK.

Covered:
1. Loading and preparing the dataset (movie reviews).
2. Shuffling documents to avoid bias.
3. Creating a frequency distribution of all words.
4. Inspecting the most common words and word frequencies.
"""

import nltk
import random
from nltk.corpus import movie_reviews

# ------------------------------------------------------
# 1. Load the dataset
# The movie_reviews corpus contains 2000 reviews:
# - 1000 positive
# - 1000 negative
#
# Each review has an ID and belongs to a category ("pos" or "neg").
# We'll create a list of tuples: (list_of_words, category).
# ------------------------------------------------------

documents = [
    (list(movie_reviews.words(fileid)), category)
    for category in movie_reviews.categories()  # categories = ['pos', 'neg']
    for fileid in movie_reviews.fileids(category)
]

# ------------------------------------------------------
# 2. Shuffle documents
# Shuffling ensures that training and testing data
# are not biased towards one category.
# ------------------------------------------------------

random.shuffle(documents)

# Let's check what a single document looks like
print("\nSample document structure (words + label):\n")
print(documents[50])  # Example: (['film', 'was', 'amazing', ...], 'pos')

# ------------------------------------------------------
# 3. Collect all words
# We'll lowercase all words to normalize them.
# Then, we'll build a frequency distribution to find
# the most common words in the corpus.
# ------------------------------------------------------

all_words = []

for w in movie_reviews.words():
    all_words.append(w.lower())

# Create frequency distribution
all_words = nltk.FreqDist(all_words)

# ------------------------------------------------------
# 4. Inspect results
# ------------------------------------------------------

print("\nTop 15 most common words:\n")
print(all_words.most_common(15))  # Shows word + frequency pairs

print("\nFrequency of the word 'stupid':", all_words["stupid"])
