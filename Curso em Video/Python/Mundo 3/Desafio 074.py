"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
"""

from random import randint

random_numbers_on_tuple = tuple(randint(1, 9) for nothing in range(5))
visualize_numbers = ', '.join([str(item) for item in random_numbers_on_tuple])
print(f"Números sorteados: {visualize_numbers}\nMaior: {max(random_numbers_on_tuple)}\nMenor: {min(random_numbers_on_tuple)}")
