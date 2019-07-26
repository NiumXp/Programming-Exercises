"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JÚNIOR
- Até 25 anos: SÊNIOR
- Acima de 25 anos: MASTER
"""

from datetime import date

actual_year = date.today().year
years_old = actual_year - int(input("Ano de nascimento: "))
print(f"O atleta tem {years_old} anos de idade.")

if years_old <= 9:
    _type = "MIRIM"
elif years_old <= 14:
    _type = "INFANTIL"
elif years_old <= 19:
    _type = "JÚNIOR"
elif years_old <= 25:
    _type = "SÊNIOR"
else:
    _type = "MASTER"
print("Classificação:", _type)
