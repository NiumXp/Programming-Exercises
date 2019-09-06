'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
'''

numbers = []
for num in range(1, 8):
    numbers.append(int(input(f"Digite o {num}º valor: ")))
numbers.sort()

print(f"Os valores pares digitados foram: {list(filter(lambda num: num % 2 == 0, numbers))}")
print(f"Os valores ímpares digitados foram: {list(filter(lambda num: num % 2 == 1, numbers))}")
