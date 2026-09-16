from fizzbuzz import fizzbuzz
from fibonacci import fibonacci
from fatorial import fatorial
from numero_primo import eh_primo
from palindromo import eh_palindromo
from tabuada import tabuada

print("exercicios de logica basica em python")

print("\nfizzbuzz ate 15:")
for item in fizzbuzz(15):
    print(item)

print("\nfibonacci, 8 termos:")
print(fibonacci(8))

print("\nfatorial de 5:", fatorial(5))

print("\nprimos ate 30:")
print([n for n in range(2, 31) if eh_primo(n)])

print("\npalindromo 'ovo':", eh_palindromo("ovo"))

print("\ntabuada do 4:")
for linha in tabuada(4):
    print(linha)
