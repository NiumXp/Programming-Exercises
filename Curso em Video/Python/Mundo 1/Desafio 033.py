"""
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

# Decidi fazer sem usar as funções `min` e `max`!

numbers = []
for position in ['Primeiro', 'Segundo', 'Terceiro']:
    numbers.append(int(input(f"{position} número: ")))

# Eu sei, não usei as funções mas usei `sorted`...
# Muito chato escrever condição atrás de condição...
numbers = sorted(numbers)

print(f"O maior é o número {numbers[-1]}!\nO menor é o número {numbers[0]}!")
