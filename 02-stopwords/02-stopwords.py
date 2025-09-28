"""
02_NLP_stopwords.py
-----------------------------------
Demonstration of removing stop words using NLTK.
"""

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary resources (only first time)
nltk.download("stopwords")
nltk.download("punkt")

# Example text (changed from the original one)
text = "NLTK is a powerful library for natural language processing tasks."

# Load English stop words
stop_words = set(stopwords.words("english"))

# Tokenize the text into words
tokens = word_tokenize(text)

# Remove stop words (case-insensitive)
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# Show results
print("Original Tokens:", tokens)
print("\nAfter Stop Word Removal:", filtered_tokens)
