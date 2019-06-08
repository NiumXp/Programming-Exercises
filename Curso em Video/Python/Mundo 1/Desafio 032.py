"""
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""

from datetime import datetime

year = int(input("Ano para analisar (0 para o atual): "))
if year == 0:
    year = datetime.now().year

if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
    is_or_no = "é"
else:
    is_or_no = "não é"

print(f"O ano {year} {is_or_no} BISSEXTO!")
