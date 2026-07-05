# Exercise 3: Word Frequency
# Count word frequencies using plain dict, defaultdict, and Counter.

from collections import Counter, defaultdict

text = "the quick brown fox jumps over the lazy dog"
words = text.split()

# 1. Plain dict
word_counts = {}
for word in words:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1
print(f"Plain dict: {word_counts}")

# 2. defaultdict(int)
word_counts2 = defaultdict(int)
for word in words:
    word_counts2[word] += 1
print(f"defaultdict: {dict(word_counts2)}")

# 3. Counter
word_counts3 = Counter(words)
print(f"Counter:     {word_counts3}")

# Counter-specific features
print(f"Most common 3: {word_counts3.most_common(3)}")
print(f"Total words: {word_counts3.total()}")

# Verify all three produce the same result
print(f"All match: {word_counts == dict(word_counts2) == dict(word_counts3)}")
