import numpy as np
from docutils.nodes import document

# 属性	含义	本例结果
# type(a)	对象类型	numpy.ndarray
# a.shape	各维度的长度	(3,)
# a.ndim	维度数量	1
# a.dtype	元素的数据类型	通常为 int64
# a.size	元素总数量	3

from src.textlab.day03.bag_of_words import vectorize

def vectorize_batch(
    texts: list[str],
    vocab: list[str]
) -> np.ndarray:
    vectors = []
    for text in texts:
        vectors.append(vectorize(text,vocab))
    result = np.array(vectors)
    return result



def main():
    texts = [
        "Python AI Python",
        "Java AI",
        "Python Java Java"
    ]
    vocab = ["ai", "java", "python"]

    result = vectorize_batch(texts, vocab)

    assert isinstance(result, np.ndarray)
    assert result.shape == (3, 3)

    assert result.tolist() == [
        [1, 0, 2],
        [1, 1, 0],
        [0, 2, 1]
    ]

    print(result)

    word_totals = result.sum(axis=0)
    document_lengths = result.sum(axis=1)
    total = result.size

    print("All tests passed!")

if __name__ == "__main__":
    main()