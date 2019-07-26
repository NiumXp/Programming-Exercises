"""
Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADO
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADO
"""

from operator import add

first_grade = float(input("Primeira nota: "))
second_grade = float(input("Segunda nota: "))
avarage = add(first_grade, second_grade) / 2

print(f"Tirando {first_grade:.1f} e {second_grade:.1f}, a média do aluno é {avarage:.1f}!")

if avarage < 5:
    status = "REPROVADO"
elif avarage > 7:
    status = "APROVADO"
else:
    status = "em RECUPERAÇÃO"
print(f"O aluna está {status}!")
