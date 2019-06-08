"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
"""

number = int(input("Digite um número entre 0 a 9999: "))
if 9999 >= number >= 0:
    print(f"""Analisando o número {number}!

Unidade: {number % 10}
Dezena: {number % 100 // 10}
Centena: {number % 1000 // 100}
Milhar: {number % 10000 // 1000}
""")
