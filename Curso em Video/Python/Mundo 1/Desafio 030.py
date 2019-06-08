"""
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""

number = int(input("Digite um número: "))
print(f"O número {number} é {'PAR' if number % 2 == 0 else 'ÍMPAR'}!")
