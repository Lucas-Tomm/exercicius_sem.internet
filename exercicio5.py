soma_pares = 0
quantidade_pares = 0

for i in range(5):
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        soma_pares = soma_pares + numero
        quantidade_pares = quantidade_pares + 1

if quantidade_pares > 0:
    media = soma_pares / quantidade_pares
    print("A média dos números pares é:", media)
else:
    print("Nenhum número par foi digitado.")
