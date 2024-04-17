import numpy as np


def monte_carlo_test(num_of_points: int) -> float:
    points = np.random.rand(num_of_points, 2)
    points = 2 * points - 1  # [0, 1] -> [-1, 1]
    pt_2 = points ** 2
    circle_in = pt_2[np.sum(pt_2, axis=1) <= 1]  # merge points x**2 + y**2 <= 1

    return len(circle_in) / num_of_points * 4


if __name__ == '__main__':
    # 1  ->  3.28
    # 10  ->  3.108
    # 100  ->  3.1384000000000003
    # 1000  ->  3.14628
    # 10000  ->  3.1425599999999996
    # 100000  ->  3.1414828000000012
    # 1000000  ->  3.1414959999999996
    # pi = 3.141592..
    for pt in range(7):
        val_10 = [monte_carlo_test(10 ** pt) for _ in range(50)]
        print(10 ** pt, ' -> ', np.mean(val_10))
