def eh_palindromo(texto):
    limpo = texto.lower().replace(" ", "")
    return limpo == limpo[::-1]


if __name__ == "__main__":
    testes = ["arara", "python", "osso", "a base do teto"]
    for t in testes:
        print(t, "->", eh_palindromo(t))
