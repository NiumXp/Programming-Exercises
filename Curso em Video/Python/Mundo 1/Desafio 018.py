"""
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""

from math import radians, sin, cos, tan

angle = radians(float(input("Digite o ângulo que desejas: ")))
print(f"""Ângulo {angle:.1f}!

SENO: {sin(angle):.2f}
COSSENO: {cos(angle):.2f}
TANGENTE: {tan(angle):.2f}""")
