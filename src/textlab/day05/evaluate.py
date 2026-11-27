import numpy as np
# from src.textlab.day05.loss import mse
from loss import mse

def evaluate_model(
    X: np.ndarray,
    y_true: np.ndarray,
    weights: np.ndarray,
    bias: float
) -> float:
    y_pred = X @ weights + bias
    return mse(y_true, y_pred)




def main():
    X = np.array([
        [1, 0, 2],
        [1, 1, 0],
        [0, 2, 1],
        [3, 0, 0]
    ])

    y_true = np.array([5.0, 3.0, 1.0, 8.0])

    weights_a = np.array([2.0, -0.5, 1.0])
    weights_b = np.array([2.5, 0.0, 1.0])

    bias = 0.5

    loss_a = evaluate_model(X, y_true, weights_a, bias)
    loss_b = evaluate_model(X, y_true, weights_b, bias)

    assert np.isclose(loss_a, 0.9375)
    assert np.isclose(loss_b, 0.0625)
    assert loss_b < loss_a

    print("Model A Loss:", loss_a)
    print("Model B Loss:", loss_b)
    print("All tests passed!")


if __name__ == "__main__":
    main()