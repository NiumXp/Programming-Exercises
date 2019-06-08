"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
"""

from math import hypot

cateto_opst = float(input("Cateto oposto: "))
cateto_adjt = float(input("Cateto adjascente: "))
print(f"A hipotenusa vai medir {hypot(cateto_opst, cateto_adjt):.2f}")
