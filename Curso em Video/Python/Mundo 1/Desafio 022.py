"""
Crie um programa que leia o nome completo de uma pessoa e mostre: 
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
"""

name = input("Digite seu nome completo: ")
print(f"""O seu nome:
    Em maiúsculas:
        {name.upper()}

    Em minúsculas:
        {name.lower()}

    Tem ao todo {len(''.join(name.split(' ')))} letras.
    E seu primeiro nome tem {len(name.split(' ')[0])} letras!
""")
