quantidade = int(input("Quantos valores?"))
valores = []
for n in range(quantidade):
        valor = float(input("Digite o valor " + str(n) + ": "))
        valores.append(valor)

print("Valores digitados:")
for numero in valores:
        print(numero)
print("Total de valores: " + str(len(valores)))

media = sum(valores) / len(valores)
print("Média: " + str(media))
