# 03-stemming-words

### 📌 Introduction
**Stemming** is a text normalization technique in Natural Language Processing (NLP).  
It reduces words to their base or root form, called the **stem**.  

The idea is simple:  
- Words like *"running"*, *"runs"*, and *"ran"* all refer to the same action.  
- Instead of treating them as different words, stemming maps them to a single root, e.g., **"run"**.  

This helps reduce redundancy in text analysis and improves efficiency when building models.

---

### 🖼 Example Output
Below is the output generated from the program:

![Stemming Output](03-stemming-words.PNG)

---

### 🚀 How to Run
You can run this file in **VS Code**, PyCharm, Jupyter Notebook, or any Python environment:

```bash
python 03-stemming-words.py
```

---

### ✅ Key Takeaways
- **Stemming** reduces words to their root form (e.g., *running → run*).  
- The **Porter Stemmer** is one of the oldest and most popular stemming algorithms.  
- It’s fast and efficient but sometimes produces stems that aren’t real words (e.g., *fairly → fairli*).  
- Despite its rough edges, stemming is widely used in search engines, indexing, and NLP pipelines.

This script demonstrates how to stem both **individual words** and a **full sentence** using NLTK’s `PorterStemmer`.
