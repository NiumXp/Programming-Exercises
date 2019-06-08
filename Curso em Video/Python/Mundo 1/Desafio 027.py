"""
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

Ex: Ana Maria de Souza (primeiro = Ana; último = Souza."""

name = input("Digite seu nome completo: ").split(' ')
print(f"Seu primeiro nome é {name[0]}\nSeu último nome é {name[-1]}")
