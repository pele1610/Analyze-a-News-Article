import re
from collections import Counter


def load_article(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return file.read()


def count_specific_word(text, word):
    words = re.findall(r'\b\w+\b', text.lower())
    return words.count(word.lower())


def identify_most_common_word(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())

    if not words:
        return None

    return Counter(words).most_common(1)[0][0]


def calculate_average_word_length(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text)

    if not words:
        return 0.0

    return round(sum(len(word) for word in words) / len(words), 2)


def count_paragraphs(text):
    if not text.strip():
        return 0

    return len(re.split(r'\n\s*\n', text.strip()))


def count_sentences(text):
    return len(re.findall(r'[.!?]+', text))


if __name__ == "__main__":
    article = load_article("news_article.txt")

    print(f"Article loaded ({len(article)} characters)")

    print("Word 'apple' appears:", count_specific_word(article, "apple"))
    print("Most common word:", identify_most_common_word(article))
    print("Average word length:", calculate_average_word_length(article))
    print("Paragraph count:", count_paragraphs(article))
    print("Sentence count:", count_sentences(article))