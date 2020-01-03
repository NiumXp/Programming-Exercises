"""
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

Ex: 
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~
"""

def escreva(texto):
    items = '~' * (len(texto) + 4)
    print("{0}\n  {1}\n{0}".format(items, texto))

escreva("Olá, Mundo!")
