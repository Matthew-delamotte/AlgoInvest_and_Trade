# Python recursive


def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)


print(factorielle(5))


def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)


print(fibo(9))
