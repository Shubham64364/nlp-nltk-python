# 05-chunking.py
# -----------------
# Demonstration of "chunking" in NLP using NLTK.
# Chunking groups words into meaningful chunks (like Noun Phrases, Verb Phrases)
# after POS (Part-of-Speech) tagging.

import nltk

# Sample sentence
sentence = "The quick brown fox jumps over the lazy dog near the river bank."

# Step 1: Tokenize the sentence (split into words)
words = nltk.word_tokenize(sentence)

# Step 2: Apply POS tagging
# Each token is tagged with a Part-of-Speech.
# Some common POS tags we'll see in this example:
#   DT  = Determiner (the, a, an)
#   JJ  = Adjective (quick, brown, lazy)
#   NN  = Noun, singular (fox, dog, bank)
#   NNS = Noun, plural (dogs, banks)
#   VB* = Verb (jumps, run, running, taken, etc.)
#   IN  = Preposition (over, near, in, on)
tagged_words = nltk.pos_tag(words)

# Step 3: Define a chunk grammar using Regular Expressions
# NP (Noun Phrase): Determiner + Adjectives + Noun
# VP (Verb Phrase): Verb followed by Noun Phrase or Prepositional Phrase
# PP (Prepositional Phrase): Preposition + Noun Phrase
chunk_grammar = r"""
  NP: {<DT>?<JJ>*<NN>}    # Noun Phrase: optional determiner, adjectives, then noun
  VP: {<VB.*><NP|PP>*}    # Verb Phrase: verb + (NP or PP)
  PP: {<IN><NP>}          # Prepositional Phrase: preposition + noun phrase
"""

# Step 4: Create a chunk parser
chunk_parser = nltk.RegexpParser(chunk_grammar)

# Step 5: Apply chunking to the tagged sentence
chunked_output = chunk_parser.parse(tagged_words)

# Step 6: Print results
print("Tagged Words:\n", tagged_words)
print("\nChunked Tree:\n", chunked_output)

# visualization:
# If you run this in an environment with GUI support, this will show the chunk tree graphically.
chunked_output.draw()
