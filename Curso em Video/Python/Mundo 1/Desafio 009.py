"""
Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
"""
input_number = int(input("Digite um número: "))

print("=" * 15)
for range_number in range(1, 11):
    print(f"{input_number} x {range_number:2} = {input_number * range_number}")
print("=" * 15) 
