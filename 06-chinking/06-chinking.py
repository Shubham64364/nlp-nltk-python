import nltk

# Sample text (2–3 lines for demonstration)
sample_text = """The quick brown fox was jumping over the lazy dog.
It enjoyed running swiftly and gracefully across the green fields."""

# Tokenize sentences
sentences = nltk.sent_tokenize(sample_text)

def process_content():
    try:
        for i in sentences:
            words = nltk.word_tokenize(i)          # Word tokenization
            tagged = nltk.pos_tag(words)           # POS tagging

            # Chunk grammar with chinking:
            # 1. First chunk everything into NP
            # 2. Then chink (remove) verbs (VB.*), prepositions (IN), determiners (DT), and 'to' (TO)
            chunkGram = r"""
                NP: {<.*>+}         
                    }<VB.?|IN|DT|TO>+{   
            """

            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)

            print("\nSentence:", i)
            print(chunked)         # Print the chunk tree
            chunked.draw()         # Graphical visualization

    except Exception as e:
        print(str(e))

process_content()
