"""
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""

from random import randint

random_number = randint(0, 5)
print("Pensei em um número entre 0 e 5!")
user_number = int(input("Qual número você que pensei? "))

if user_number == random_number:
    print("Você acertou!")
else:
    print(f"Eu pensei no número {random_number} não no {user_number}!")
