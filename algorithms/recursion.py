def power(base, pow):
    if pow == 0:
        return 1
    elif pow == 1:
        return base
    else:
        return base * power(base, pow - 1)


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    print(factorial(6))
    print(power(2, 20))
