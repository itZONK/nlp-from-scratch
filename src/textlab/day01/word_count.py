from operator import truediv


def word_count(text):
    words = text.split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts


def top_k(counts, k):
    result = sorted(counts.items(), key=lambda item: item[1], reverse=True)
    return result[:k]

def sort_student(students):
    for student in students
        student[1]

def main():
    # text = "python java python ai java python"
    # counts = word_count(text)
    # print(counts)
    # text2 = "python python java"
    # counts = word_count(text2)
    # print(counts)
    # text3 = ""
    # counts = word_count(text3)
    # print(counts)

    counts = {
        "python": 3,
        "java": 2,
        "ai": 1,
        "nlp": 5
    }

    result = top_k(counts, 2)
    print(result)


if __name__ == "__main__":
    main()
