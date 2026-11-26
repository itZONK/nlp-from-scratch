import numpy as np


from src.textlab.day04.numpy_intro import vectorize_batch

def validate_text(
        texts:list[str],
        vocab:list[str],
        weights:np.array([]),
        baids:int
    ):
    w = vectorize_batch(texts,vocab)
    w = w.sum(axis=0)
    return w @ weights + baids


def main():
    texts = [
        "Python AI Python",
        "Java AI",
        "Python Java Java",
        "AI AI AI"
    ]

    vocab = ["ai", "java", "python"]

    weights = np.array([2.0, -0.5, 1.0])

    bias = 0.5

    print(validate_text(texts,vocab,weights,bias))



if __name__ == "__main__":
     main()