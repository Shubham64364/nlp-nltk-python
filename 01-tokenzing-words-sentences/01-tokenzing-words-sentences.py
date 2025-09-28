# ============================
# Natural Language Processing Basics with NLTK
# ============================

# Download NLTK resources (only once needed)
# nltk.download() # Opens NLTK Downloader GUI, clcick "all" to download all resources at once
# nltk.download('punkt')   # Punkt tokenizer models

# Import required library
import nltk



# --------------------------------------------------
# Key NLP Concepts:
# 1) Tokenization  → Splitting text into words or sentences
# 2) Lexicon       → Vocabulary of a language (words + meanings)
#    Example: "bull" = animal (general) OR "bull" = optimistic investor (finance)
# 3) Semantics     → Study of word meanings in context
# 4) Corpora       → Large collection of texts (e.g., medical journals, news articles)
# --------------------------------------------------

from nltk.tokenize import word_tokenize, sent_tokenize

# Sample text
sample_text = """
Hello Mr. Basit, how are you? 
Hope everything is going well. 
When will you be free today so we can discuss our project?
"""

# Word Tokenization
words = word_tokenize(sample_text)
print("Word Tokenization:")
print(words)
print("\n--------------------------------------\n")

# Sentence Tokenization
sentences = sent_tokenize(sample_text)
print("Sentence Tokenization:")
print(sentences)

# Extra: Iterating over tokens (alternative style)
print("\Words printed one by one:")
for token in words:
    print(token)
