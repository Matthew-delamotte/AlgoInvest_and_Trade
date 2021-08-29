# Python recursive


def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)


# print(factorielle(5))


def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


# print(fibo(9))


data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20 ]
 
def combinations(n, k, min_n=0, accumulator=None):
    if accumulator is None:
        accumulator = []
    if k == 0:
        return [accumulator]
    else:
        return [l for x in range(min_n, n)
                for l in combinations(n, k - 1, x + 1, accumulator + [x + 1])]

result = combinations(len(data), 10)

