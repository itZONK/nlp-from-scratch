import numpy as np

def mse(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    # 使用直接做差，求平方判断loss
    loss_a =  y_pred - y_true
    return (loss_a ** 2).mean()

def mae(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    loss_a = y_pred - y_true
    return (np.abs(loss_a)).mean()

# 

def main():
    y_true = np.array([5.0, 3.0, 1.0, 8.0])

    y_pred_a = np.array([4.0, 2.0, 0.0, 7.0])
    y_pred_b = np.array([6.0, 4.0, 0.0, 7.0])
    y_pred_c = np.array([5.0, 3.0, 1.0, 12.0])

    # MSE 测试
    assert np.isclose(mse(y_true, y_pred_a), 1.0)
    assert np.isclose(mse(y_true, y_pred_b), 1.0)
    assert np.isclose(mse(y_true, y_pred_c), 4.0)

    # MAE 测试
    assert np.isclose(mae(y_true, y_pred_a), 1.0)
    assert np.isclose(mae(y_true, y_pred_b), 1.0)
    assert np.isclose(mae(y_true, y_pred_c), 1.0)

    # 完美预测测试
    assert np.isclose(mse(y_true, y_true), 0.0)
    assert np.isclose(mae(y_true, y_true), 0.0)

    print("All tests passed!")


if __name__ == "__main__":
    main()