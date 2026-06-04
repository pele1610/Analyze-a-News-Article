import re

def load_article(filename):
    file = open(filename, "r", encoding="utf-8")
    text = file.read()
    file.close()
    return text

def count_specific_word(text, word):
    words = re.findall(r"\w+", text.lower())

    count = 0

    for w in words:
        if w == word.lower():
            count += 1
        else:
            count += 0

    return count

def identify_most_common_word(text):
    if text.strip() == "":
        return None

    words = re.findall(r"[a-zA-Z]+", text.lower())

    most_common = None
    highest_count = 0

    for word in words:
        current_count = words.count(word)

        if current_count > highest_count:
            highest_count = current_count
            most_common = word
        else:
            pass

    return most_common

def calculate_average_word_length(text):
    if text.strip() == "":
        return 0

    words = re.findall(r"[a-zA-Z]+", text)

    total = 0

    for word in words:
        total = total + len(word)

    average = total / len(words)

    return round(average, 2)

def count_paragraphs(text):
    if text.strip() == "":
        return 1

    paragraphs = text.strip().split("\n\n")

    count = 0

    for paragraph in paragraphs:
        if paragraph.strip() != "":
            count += 1
        else:
            pass

    return count


def count_sentences(text):
    if text.strip() == "":
        return 1

    endings = re.findall(r"[.!?]", text)

    count = 0
    i = 0

    while i < len(endings):
        count += 1
        i += 1

    return count

if __name__ == "__main__":

    article = load_article("news_article.txt")

    print("Article loaded (" + str(len(article)) + " characters)")

    search_word = "apple"

    print("Occurrences of '" + search_word + "':",
          count_specific_word(article, search_word))

    print("Most common word:",
          identify_most_common_word(article))

    print("Average word length:",
          calculate_average_word_length(article))

    print("Paragraph count:",
          count_paragraphs(article))

    print("Sentence count:",
          count_sentences(article))