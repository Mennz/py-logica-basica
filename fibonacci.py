def fibonacci(n):
    sequencia = []
    a, b = 0, 1
    for _ in range(n):
        sequencia.append(a)
        a, b = b, a + b
    return sequencia


if __name__ == "__main__":
    print(fibonacci(10))
