valor1 = float(input("Digite um número:"))
valor2 = float(input("Digite outro número:"))
valor3 = float(input("Digite outro número:"))
valores = [valor1, valor2, valor3]

print("Valores digitados:")
for valor in valores:
    print(valor)

media = sum(valores) / len(valores)
print("Média: " + str(media))