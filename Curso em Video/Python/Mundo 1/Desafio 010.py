"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
"""

money = float(input("Eu tenho R$"))
print(f"Eu teria U${round(money / 3.89):.2f}!")
