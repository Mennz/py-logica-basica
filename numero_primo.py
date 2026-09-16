def eh_primo(n):
    if n < 2:
        return False
    # so precisa testar ate a raiz quadrada
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    primos = [n for n in range(2, 50) if eh_primo(n)]
    print(primos)
