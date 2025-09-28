# ============================
# Lemmatization with NLTK
# ============================

import nltk
from nltk.stem import WordNetLemmatizer

# Ensure WordNet is downloaded once
# nltk.download('wordnet')
# nltk.download('omw-1.4')

lemmatizer = WordNetLemmatizer()

# Example words to lemmatize
words = ["cars", "wolves", "running", "better", "studies", "flying"]

print("Lemmatization Examples:\n")

for word in words:
    # Show lemma as noun
    print(f"{word} (noun) -> {lemmatizer.lemmatize(word)}")

# Showing how POS affects output
print("\nPOS-specific examples:")
print("running (verb) ->", lemmatizer.lemmatize("running", pos="v"))
print("better (adjective) ->", lemmatizer.lemmatize("better", pos="a"))
print("studies (verb) ->", lemmatizer.lemmatize("studies", pos="v"))
