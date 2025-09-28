# 13-naive-bayes-classifier.py
"""
Naive Bayes Classifier with NLTK
--------------------------------
This script extends the word-to-features step and demonstrates:
1. Splitting data into training and testing sets.
2. Training a Naive Bayes classifier.
3. Checking the model’s accuracy.
4. Displaying the most informative features.
"""

import nltk
import random
from nltk.corpus import movie_reviews

# ------------------------------------------------------
# 1. Prepare dataset (same as before)
documents = [
    (list(movie_reviews.words(fileid)), category)
    for category in movie_reviews.categories()
    for fileid in movie_reviews.fileids(category)
]

random.shuffle(documents)

# ------------------------------------------------------
# 2. Build frequency distribution of words
all_words = []
for w in movie_reviews.words():
    all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
word_features = list(all_words.keys())[:3000]  # top 3000 words

# ------------------------------------------------------
# 3. Function to convert review to feature dictionary
def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

# Build the final feature sets
featuresets = [(find_features(rev), category) for (rev, category) in documents]

print("Total feature sets:", len(featuresets))  # should be 2000

# ------------------------------------------------------
# 4. Split into training (1900) and testing (100)
training_set = featuresets[:1900]
testing_set = featuresets[1900:]

# ------------------------------------------------------
# 5. Train Naive Bayes Classifier
classifier = nltk.NaiveBayesClassifier.train(training_set)

# ------------------------------------------------------
# 6. Evaluate accuracy
accuracy = nltk.classify.accuracy(classifier, testing_set) * 100
print(f"Naive Bayes Classifier Accuracy: {accuracy:.2f}%")

# ------------------------------------------------------
# 7. Show most informative features
classifier.show_most_informative_features(15)
