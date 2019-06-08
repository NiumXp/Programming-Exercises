"""
O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

from random import shuffle

students = []
for position in ["Primeiro", "Segundo", "Terceiro", "Quarto"]:
    students.append(input(f"{position} aluno: "))
shuffle(students)
print(f"A ordem de apresentação será {students}")
