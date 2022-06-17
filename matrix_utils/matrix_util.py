import numpy as np


def get_sqrt_matrix(x: np.ndarray) -> np.ndarray:
    """
    Find matrix A, inverse of X such that A**2 = X
    Let D = S^-1XS. Since E = S^-1S, then D = S^-1AEAS = (S^-1AS)**2
    Let A' = S^-1AS. It leads that A'D = A'**3 = A'**2 A' = DA'

    A' is diagonalizable, so let A' = diag(a, b, c)
    Elements of diagonal matrix A' are square root of eigen values of X
    A' = S^-1AS follows that A = SA'S^-1, such that A**2 = X

    e.g)
    A = np.array([[1, 0, 0], [0, 1, 0], [1, 2, 3]])
    sq_A = get_sqrt_matrix(A)
    print(sq_A.dot(sq_A))

    Note) scipy.linalg.sqrtm

    :param x: array_like N*N
    :return: sqrt matrix A of x such that A**2 = x
    """

    eiv, s = np.linalg.eig(x)
    s_inv = np.linalg.inv(s)

    return s.dot(np.diag(np.sqrt(eiv))).dot(s_inv)