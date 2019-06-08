"""
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
"""

# Usei `str` porque "todas as informações possíveis" ??

_input = input("Digite algo: ")

print(f"""
Tipo: {type(_input)}

Alfanumérico? {_input.isalnum()}
Letra? {_input.isalpha()}
Ascii? {_input.isascii()}
Decimal? {_input.isdecimal()}
Digito? {_input.isdigit()}
Minúsculas? {_input.islower()}
Número? {_input.isnumeric()}
Espaço? {_input.isspace()}
Título? {_input.istitle()}
Maiúsculas? {_input.isupper()}
""")
