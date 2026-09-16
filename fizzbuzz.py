def fizzbuzz(n):
    resultado = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            resultado.append("fizzbuzz")
        elif i % 3 == 0:
            resultado.append("fizz")
        elif i % 5 == 0:
            resultado.append("buzz")
        else:
            resultado.append(str(i))
    return resultado


if __name__ == "__main__":
    for item in fizzbuzz(20):
        print(item)
