"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
"""

salary = float(input("Salário: "))
new_salary = salary
new_salary += salary * 15 / 100 if salary < 1250 else salary * 10 / 100
print(f"Quem ganhava R${salary:.2f} passa a ganhar {new_salary:.2f}")
