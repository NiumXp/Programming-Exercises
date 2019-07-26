"""
Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
1 para binário,
2 para octal e 3 para hexadecimal.
"""

number = int(input("Digite um número inteiro: "))
print("""Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL""")
decision = int(input("Sua opção: "))

if decision in [1, 2, 3]:
    if decision == 1:
        number_converted = bin(number)
        _type = "BINÁRIO"
    elif decision == 2:
        number_converted = oct(number)
        _type = "OCTAL"
    elif decision == 3:
        number_converted = hex(number)
        _type = "HEXADECIMAL"
    print(f"{number} convertido para {_type} é igual a {str(number_converted)[2:]}")
else:
    print("Opção inválida, tente novamente.")
