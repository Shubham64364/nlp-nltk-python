# 12-converting-words-to-features.py
"""
Converting Words to Features for Text Classification
----------------------------------------------------
This script demonstrates how to:
1. Load the NLTK movie_reviews corpus.
2. Build a vocabulary of the most frequent words (top 3000).
3. Convert each review into a feature dictionary (word presence → True/False).
4. Build the final dataset (features + label) for training classifiers.
"""

import nltk
import random
from nltk.corpus import movie_reviews

# ------------------------------------------------------
# 1. Prepare the dataset (documents with words + labels)
# documents = [ (list_of_words_in_review, "pos/neg"), ... ]
documents = [
    (list(movie_reviews.words(fileid)), category)
    for category in movie_reviews.categories()
    for fileid in movie_reviews.fileids(category)
]

# Shuffle to avoid bias (otherwise all neg come first, then pos)
random.shuffle(documents)

print("Sample document structure:\n", documents[0], "\n")

# ------------------------------------------------------
# 2. Build the frequency distribution of all words
all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

# Create frequency distribution (counts word occurrences)
all_words = nltk.FreqDist(all_words)

print("15 Most Common Words:\n", all_words.most_common(15), "\n")
print("Frequency of the word 'stupid':", all_words["stupid"], "\n")

# ------------------------------------------------------
# 3. Select the top 3000 most frequent words as features
word_features = list(all_words.keys())[:3000]
print("Top 10 word features:\n", word_features[:10], "\n")

# ------------------------------------------------------
# 4. Function to convert a document into feature dictionary
def find_features(document):
    """
    Input: document (list of words from one review)
    Output: dictionary { 'word': True/False, ... } for top 3000 words
    """
    words = set(document)  # convert to set for faster lookup
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

# Example usage on one review:
print("Features for first negative review:\n")
print(find_features(movie_reviews.words('neg/cv000_29416.txt')))
print("\n")

# ------------------------------------------------------
# 5. Build featuresets (feature_dict + label)
# featuresets = [ ({'word1': True, 'word2': False, ...}, 'pos/neg'), ... ]
featuresets = [(find_features(rev), category) for (rev, category) in documents]

print("Number of feature sets created:", len(featuresets))
print("Example feature set:\n", featuresets[0])
