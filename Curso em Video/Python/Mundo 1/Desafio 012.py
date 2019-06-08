"""
Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

price_of_product = float(input("Preço do produto: "))
print(f"O preço R${price_of_product:.2f} com desconto de 5% fica R${price_of_product * 5 / 100}!")
