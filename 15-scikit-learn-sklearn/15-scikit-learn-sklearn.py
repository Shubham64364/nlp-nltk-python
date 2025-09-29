# 15-scikit-learn-sklearn.py
# Using Scikit-Learn classifiers with NLTK for sentiment analysis

import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier

# Scikit-learn models
from sklearn.naive_bayes import MultinomialNB, BernoulliNB
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.svm import SVC, LinearSVC, NuSVC

# -----------------------------
# Preparing the dataset
# -----------------------------
# Load documents with their category (pos/neg)
documents = [(list(movie_reviews.words(fileid)), category)
             for category in movie_reviews.categories()
             for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)

# Build frequency distribution of words
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())

# Take the top 3000 words as features
word_features = list(all_words.keys())[:3000]

# Function to extract features from a document
def find_features(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
    return features

# Create feature sets for all documents
featuresets = [(find_features(rev), category) for (rev, category) in documents]

# Split into training and testing sets
training_set = featuresets[:1900]
testing_set = featuresets[1900:]

# -----------------------------
# Original Naive Bayes Classifier
# -----------------------------
classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Original Naive Bayes Algo accuracy percent:",
      (nltk.classify.accuracy(classifier, testing_set)) * 100)

classifier.show_most_informative_features(15)

# -----------------------------
# Scikit-Learn Classifiers
# -----------------------------
# Multinomial Naive Bayes
MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier accuracy percent:",
      (nltk.classify.accuracy(MNB_classifier, testing_set)) * 100)

# Bernoulli Naive Bayes
BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("BernoulliNB_classifier accuracy percent:",
      (nltk.classify.accuracy(BernoulliNB_classifier, testing_set)) * 100)

# Logistic Regression
LogisticRegression_classifier = SklearnClassifier(LogisticRegression(max_iter=200))
LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier accuracy percent:",
      (nltk.classify.accuracy(LogisticRegression_classifier, testing_set)) * 100)

# Stochastic Gradient Descent Classifier
SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print("SGDClassifier_classifier accuracy percent:",
      (nltk.classify.accuracy(SGDClassifier_classifier, testing_set)) * 100)

# Support Vector Classifier
SVC_classifier = SklearnClassifier(SVC())
SVC_classifier.train(training_set)
print("SVC_classifier accuracy percent:",
      (nltk.classify.accuracy(SVC_classifier, testing_set)) * 100)

# Linear Support Vector Classifier
LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier accuracy percent:",
      (nltk.classify.accuracy(LinearSVC_classifier, testing_set)) * 100)

# Nu-Support Vector Classifier
NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC_classifier accuracy percent:",
      (nltk.classify.accuracy(NuSVC_classifier, testing_set)) * 100)
