"""
Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
"""
from math import sqrt

number = int(input("Digite um número: "))
print(f"O dobro de {number} é {number * 2}, o triplo é {number * 3} e sua raiz é {round(sqrt(number))}")
