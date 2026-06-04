import re
from collections import Counter


def load_article(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def count_specific_word(text, word):
    words = re.findall(r'\b\w+\b', text.lower())

    count = 0

    for w in words:
        if w == word.lower():
            count += 1
        else:
            count += 0

    return count


def identify_most_common_word(text):
    if not text.strip():
        return None

    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    if not words:
        return None

    counts = Counter(words)

    most_common = None
    highest_count = 0

    for word, frequency in counts.items():
        if frequency > highest_count:
            highest_count = frequency
            most_common = word
        else:
            pass

    return most_common


def calculate_average_word_length(text):
    if not text.strip():
        return 0

    words = re.findall(r'\b[a-zA-Z]+\b', text)

    if not words:
        return 0

    total_length = 0

    for word in words:
        total_length += len(word)

    return round(total_length / len(words), 2)


def count_paragraphs(text):
    if not text.strip():
        return 1

    paragraphs = re.split(r'\n\s*\n', text.strip())

    count = 0

    for paragraph in paragraphs:
        if paragraph.strip():
            count += 1
        else:
            pass

    return count


def count_sentences(text):
    if not text.strip():
        return 1

    sentences = re.findall(r'[.!?]+', text)

    if not sentences:
        return 1

    count = 0
    index = 0

    while index < len(sentences):
        count += 1
        index += 1

    return count


if __name__ == "__main__":
    article = load_article("news_article.txt")

    print(f"Article loaded ({len(article)} characters)")

    search_word = "apple"

    print(f"Occurrences of '{search_word}':",
          count_specific_word(article, search_word))

    print("Most common word:",
          identify_most_common_word(article))

    print("Average word length:",
          calculate_average_word_length(article))

    print("Paragraph count:",
          count_paragraphs(article))

    print("Sentence count:",
          count_sentences(article))