from collections import Counter
from itertools import count
import re


def vectorize(text: str, vocab: list[str]) -> list[int]:
    words = re.findall(r"[a-z]+", text.lower())
    counts = Counter(words)
    list1 = []

    for item in vocab:
        list1.append(counts.get(item, 0))

    return list1



def main():
    vocab = ["ai", "java", "python"]

    assert vectorize("Python, AI! Python.", vocab) == [1, 0, 2]

    assert vectorize("Java JAVA AI", vocab) == [1, 2, 0]

    assert vectorize("Hello world!", vocab) == [0, 0, 0]

    assert vectorize("", vocab) == [0, 0, 0]

    assert vectorize("Python AI", ["python", "ai"]) == [1, 1]

    print("All tests passed!")

if __name__ == "__main__":
     main()