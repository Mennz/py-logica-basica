def fatorial(n):
    if n < 0:
        raise ValueError("nao existe fatorial de numero negativo")
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


if __name__ == "__main__":
    for i in range(6):
        print(f"{i}! = {fatorial(i)}")
