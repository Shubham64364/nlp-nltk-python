# 10-wordnet.py
"""
WordNet with NLTK
-----------------
This script demonstrates various features of WordNet integrated with NLTK.

Covered:
1. Exploring synsets (sets of synonyms).
2. Extracting word definitions and usage examples.
3. Synonyms and antonyms.
4. Hypernyms (broader categories) and hyponyms (narrower categories).
5. Holonyms (whole-part relations) and meronyms (part-of relations).
6. Verb entailments.
7. Derivationally related forms.
8. Semantic similarity comparisons between words.
"""

from nltk.corpus import wordnet

# ------------------------------------------------------
# 1. Synsets Lookup

print("\n Synsets for the word 'program':")
syns = wordnet.synsets("program")
print(syns)  # list of synsets

print("\nFirst synset name (identifier):", syns[0].name())
print("First lemma of first synset:", syns[0].lemmas()[0].name())
print("Definition:", syns[0].definition())
print("Example sentences:", syns[0].examples())

# ------------------------------------------------------
# 2. Synonyms and Antonyms

print("\n Synonyms and Antonyms for 'good':")
synonyms, antonyms = [], []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print("Unique Synonyms:", set(synonyms))
print("Unique Antonyms:", set(antonyms))

# ------------------------------------------------------
# 3. Hypernyms & Hyponyms

dog = wordnet.synset("dog.n.01")

print("Hypernyms (broader categories):", dog.hypernyms())
print("Hyponyms (narrower categories):", dog.hyponyms())

print("\nExample hypernym paths:")
for path in dog.hypernym_paths():
    print(" → ".join([synset.name().split('.')[0] for synset in path]))

# ------------------------------------------------------
# 4. Verb Entailments

print("\n Verb Entailments of 'snore':")
snore = wordnet.synset("snore.v.01")
print("Entailments:", snore.entailments())

# ------------------------------------------------------
# 5. Semantic Similarity
print("\n Semantic Similarity Comparisons:")

# Ship vs Boat
w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")
print(f"Similarity(ship, boat) [Wu-Palmer]: {w1.wup_similarity(w2)}")
print(f"Similarity(ship, boat) [Path]: {w1.path_similarity(w2)}")

# Ship vs Car
w2 = wordnet.synset("car.n.01")
print(f"Similarity(ship, car) [Wu-Palmer]: {w1.wup_similarity(w2)}")
print(f"Similarity(ship, car) [Path]: {w1.path_similarity(w2)}")

# Ship vs Cat
w2 = wordnet.synset("cat.n.01")
print(f"Similarity(ship, cat) [Wu-Palmer]: {w1.wup_similarity(w2)}")
print(f"Similarity(ship, cat) [Path]: {w1.path_similarity(w2)}")


