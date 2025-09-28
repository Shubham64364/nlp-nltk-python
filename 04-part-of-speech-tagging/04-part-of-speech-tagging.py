# ============================
# Part of Speech (POS) Tagging with NLTK
# ============================

import nltk
from nltk.corpus import inaugural
from nltk.tokenize import PunktSentenceTokenizer

# --------------------------------------------------
# Training and testing text (smaller inaugural speeches)
# --------------------------------------------------
# Training text: George Washington's 1789 inaugural address
train_text = inaugural.raw("1789-Washington.txt")

# Sample/test text: George Washington's 1793 inaugural address
sample_text = inaugural.raw("1793-Washington.txt")

# --------------------------------------------------
# Train a custom sentence tokenizer on the training text
# --------------------------------------------------
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

# Tokenize the sample/test text into sentences
tokenized = custom_sent_tokenizer.tokenize(sample_text)

# --------------------------------------------------
# Function to process and tag POS for first ~40 words
# --------------------------------------------------
def process_content():
    try:
        word_count = 0  # to stop after ~40 words
        for sentence in tokenized:
            words = nltk.word_tokenize(sentence)  # tokenize sentence into words
            tagged = nltk.pos_tag(words)          # assign POS tags

            for pair in tagged:
                print(pair)
                word_count += 1
                if word_count >= 40:  # limit output
                    return
    except Exception as e:
        print(str(e))


# Run the function
process_content()
