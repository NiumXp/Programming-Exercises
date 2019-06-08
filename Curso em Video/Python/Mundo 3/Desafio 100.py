"""
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
"""

from random import randint

def sorteia():
    return [randint(1, 9) for nothing in range(5)]

print("Sorteando valores: ", end="")
números = sorteia()
print(números, "PRONTO!")

def somaPar():
    new_números = []
    for index in range(len(números)):
        if números[index] % 2 == 0:
            new_números.append(números[index])
    return sum(new_números)

print(f"A soma dos pares de {números} é {somaPar()}")
