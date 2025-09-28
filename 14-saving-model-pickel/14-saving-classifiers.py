# 14-saving-classifiers.py
"""
Saving and Loading Classifiers with Pickle
------------------------------------------
This script shows how to:
1. Train a Naive Bayes classifier (using movie reviews).
2. Save the trained model to a file using pickle.
3. Load the classifier back from file.
4. Test the loaded model to confirm it works correctly.
"""

import nltk
import random
import pickle
from nltk.corpus import movie_reviews

# ------------------------------------------------------
# 1. Prepare dataset
documents = [
    (list(movie_reviews.words(fileid)), category)
    for category in movie_reviews.categories()
    for fileid in movie_reviews.fileids(category)
]
random.shuffle(documents)

# ------------------------------------------------------
# 2. Build frequency distribution
all_words = [w.lower() for w in movie_reviews.words()]
all_words = nltk.FreqDist(all_words)
word_features = list(all_words.keys())[:3000]

# ------------------------------------------------------
# 3. Feature extraction
def find_features(document):
    words = set(document)
    return {w: (w in words) for w in word_features}

featuresets = [(find_features(rev), category) for (rev, category) in documents]

# ------------------------------------------------------
# 4. Split into training & testing
training_set = featuresets[:1900]
testing_set = featuresets[1900:]

# ------------------------------------------------------
# 5. Train Naive Bayes Classifier
classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Original Classifier Accuracy:", nltk.classify.accuracy(classifier, testing_set) * 100, "%")

# ------------------------------------------------------
# 6. Save the classifier using pickle
save_classifier = open("naivebayes.pickle", "wb")
pickle.dump(classifier, save_classifier)
save_classifier.close()
print("Classifier saved as naivebayes.pickle")

# ------------------------------------------------------
# 7. Load the classifier back
load_classifier = open("naivebayes.pickle", "rb")
loaded_classifier = pickle.load(load_classifier)
load_classifier.close()

# ------------------------------------------------------
# 8. Test loaded classifier
print("Loaded Classifier Accuracy:", nltk.classify.accuracy(loaded_classifier, testing_set) * 100, "%")
loaded_classifier.show_most_informative_features(10)
