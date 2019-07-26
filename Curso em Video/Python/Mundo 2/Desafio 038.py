"""
Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
"""

first_number = int(input("Primeiro número: "))
second_number = int(input("Segundo número: "))

if first_number > second_number:
    print("O PRIMERIO número é o maior.")
elif first_number < second_number:
    print("O SEGUNDO número é o maior.")
else:
    print("Os valores são iguais.")
