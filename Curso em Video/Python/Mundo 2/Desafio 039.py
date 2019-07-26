"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""

from datetime import datetime

actual_year = datetime.now().year
year_of_birth = int(input("Ano de nascimento: "))
years_old = actual_year - year_of_birth
print(f"Quem nasceu em {year_of_birth} tem {years_old} anos em {actual_year}.")

if years_old < 18:
    years = 18 - years_old
    print(f"Ainda faltam {years} anos para o seu alistamento, que será em {years + actual_year}.")
elif years_old > 18:
    years = years_old - 18
    print(f"Você já deveria ter se alistado a {years} anos.\nSeu alistamento foi em {actual_year - years}.")
else:
    print("Você tem que se alistar IMEDIATAMENTE!")
