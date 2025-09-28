import nltk
from nltk.corpus import movie_reviews

# Make sure corpus is downloaded
# nltk.download("movie_reviews")

# The movie_reviews corpus has two categories: pos (positive) and neg (negative)
print("Categories:", movie_reviews.categories())

# Get file IDs (list of documents in the corpus)
print("\nSample file IDs:", movie_reviews.fileids()[:5])

# Access words from a specific file
file_id = movie_reviews.fileids()[0]
print(f"\nWords in first file ({file_id}):")
print(movie_reviews.words(file_id)[:20])

# Access raw text
print(f"\nRaw text of first file ({file_id}):")
print(movie_reviews.raw(file_id)[:200])

# Show where the corpus is stored on your computer
print("\nNLTK data path:")
print(nltk.data.path)
