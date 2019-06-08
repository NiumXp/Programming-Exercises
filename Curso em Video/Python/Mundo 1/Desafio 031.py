"""
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas."""

distance = int(input("Distância da viagem: "))
price_of_travel = distance * 0.50 if distance < 200 else distance * 0.45
print(f"Você irá viajar {distance:.1f}Km! E pagará R${price_of_travel:.2f}!")
