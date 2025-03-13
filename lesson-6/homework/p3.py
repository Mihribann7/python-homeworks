import os
from collections import Counter
import string

if not os.path.isfile("sample.txt"):
    print("sample.txt not found. Please enter a paragraph to create it.")
    with open("sample.txt", "w") as file:
        file.write(input("Enter your paragraph: ") + "\n")

with open("sample.txt", "r") as file:
    content = file.read().lower()


content = content.translate(str.maketrans("", "", string.punctuation))

words = content.split()

word_count = Counter(words)

total_words = sum(word_count.values())

top_words = word_count.most_common(5)

print(f"Total words: {total_words}")
print("Top 5 most common words:")
for word, count in top_words:
    print(f"{word} - {count} {'time' if count == 1 else 'times'}")

with open("word_count_report.txt", "w") as report:
    report.write("Word Count Report\n")
    report.write(f"Total Words: {total_words}\n")
    report.write("Top 5 Words:\n")
    for word, count in top_words:
        report.write(f"{word} - {count}\n")

print("\nReport saved to 'word_count_report.txt'")
