"""
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
"""

city = input("Cidade: ").rstrip().upper()
print(city.startswith("SANTO"))
