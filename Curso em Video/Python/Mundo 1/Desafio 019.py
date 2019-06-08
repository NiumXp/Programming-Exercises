"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
"""

from random import choice

students = []
for position in ["Primeiro", "Segundo", "Terceiro", "Quarto"]:
    students.append(input(f"{position} aluno: "))
print(f"O aluno escolhido foi {choice(students)}")
