# Stemming words with NLTK

from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Initialize the Porter Stemmer
ps = PorterStemmer()

# Example words with similar roots
example_words = ["running", "runner", "runs", "easily", "fairly"]

print("example word stemming:")
for w in example_words:
    print(f"{w} -> {ps.stem(w)}")

print("\n sentence stemming:")

# Example sentence
new_text = "The runners were running easily, and they fairly enjoyed their run."

# Tokenize the sentence into words
words = word_tokenize(new_text)

# Apply stemming to each word
for w in words:
    print(f"{w} -> {ps.stem(w)}")
