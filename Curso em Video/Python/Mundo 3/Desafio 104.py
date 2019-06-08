"""
Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante 'a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n: ')
"""

def leiaInt(prompt):
    while True:
        try:
            numero = int(input(prompt))
        except ValueError:
            print("ERRO! Digite um número inteiro válido.")
        else:
            return numero

n = leiaInt("Digite um número: ")
print(f"Você digitou o número {n}!")
