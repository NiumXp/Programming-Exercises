"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

salary = float(input("Sálario do funcionário? R$"))
print(f"R${salary:.2f} com 15% de aumento fica R${salary + salary * 15 / 100:.2f}!")
