def tabuada(numero):
    linhas = []
    for i in range(1, 11):
        linhas.append(f"{numero} x {i} = {numero * i}")
    return linhas


if __name__ == "__main__":
    for linha in tabuada(7):
        print(linha)
