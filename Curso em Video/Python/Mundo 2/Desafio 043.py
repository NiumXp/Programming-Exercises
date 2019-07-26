"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
- IMC abaixo de 18,5: Abaixo do Peso
- Entre 18,5 e 25: Peso Ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade Mórbida
"""

weight = float(input("Qual é o seu peso? (Kg) "))
height = float(input("Qual a sua altura? (m) "))
imc = weight / pow(height, 2)

print(f"O IMC dessa pessoa é de {imc:.1f}")

if imc < 18.5:
    status = "ABAIXO DO PESO"
elif imc < 25:
    status = "no PESO IDEAL"
elif imc < 30:
    status = "com SOBREPESO"
elif imc < 40:
    status = "com OBESIDADE"
else:
    status = "com OBESIDADE MÓRBIDA"
print(f"A pessoa está {status}!")
