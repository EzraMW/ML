import numpy as np
from numpy.linalg import matrix_power


def fib_rec(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

def fib_imp(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    num1 = 1
    num2 = 1
    fib = 0
    for i in range(2, n):
        fib = num1 + num2
        num1 = num2
        num2 = fib
    return fib

def fib_matrix(n):
    matrix = np.array([[1, 1], [1, 0]])
    return matrix_power(matrix, n)[0][1]


if __name__ == '__main__':
    print("running 3 methods for fibonacci with example n = 19")
    print("recursive fibonacci method: " + str(fib_rec(19)))
    print("imperative fibonacci method: " + str(fib_imp(19)))
    print("matrix fibonacci method: " + str(fib_matrix(19)))

