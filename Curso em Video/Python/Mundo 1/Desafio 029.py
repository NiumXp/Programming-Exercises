"""
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
"""

velocity_of_car = int(input("Qual é a velocidade do carro? "))
if velocity_of_car > 80:
    velocity_of_car -= 80
    print(f"MULTADO! Você irá pagar R${velocity_of_car * 7:.2f} por ultrapassar 80Km/h!")
print("Dirija com segurança, tenha um bom dia!")
