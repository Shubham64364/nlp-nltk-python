# 07-named-entity-recognition.py
"""
Named Entity Recognition (NER) Example with NLTK

This script demonstrates Named Entity Recognition (NER) on a small sample text.
NER automatically detects names of people, organizations, locations, etc.
"""

import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# Example text (short and simple)
sample_text = """
Barack Obama was the 44th President of the United States.
He gave a speech in Berlin and met with Angela Merkel.
Later, he visited Microsoft headquarters in Washington.
"""

# Split text into sentences
sentences = sent_tokenize(sample_text)

def process_content():
    try:
        for i in sentences:
            words = word_tokenize(i)       # tokenize words
            tagged = nltk.pos_tag(words)   # POS tagging
            namedEnt = nltk.ne_chunk(tagged, binary=False)  # binary=False → shows exact NE labels
            print(namedEnt)     # print tree structure in console
            namedEnt.draw()     # tree visualization popup
    except Exception as e:
        print(str(e))

process_content()
