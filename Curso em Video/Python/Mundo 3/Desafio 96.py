"""
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.
""

def área(largura, comprimento):
  return largura * comprimento

largura = float(input("Largura (m): "))
comprimento = float(input("Comprimento (m): "))

a = área(largura, comprimento)

print("A área de um terreno {largura:.1f}x{comprimento:.1f} é de {a:.1f}²!")
