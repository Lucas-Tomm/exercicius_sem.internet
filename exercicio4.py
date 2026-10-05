quantidade_pares = 0
quantidade_impares = 0
soma_pares = 0
soma_impares = 0

for i in range(10):
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
        quantidade_pares = quantidade_pares + 1
        soma_pares = soma_pares + numero
    else:
        quantidade_impares = quantidade_impares + 1
        soma_impares = soma_impares + numero

print("Quantidade de pares:", quantidade_pares)
print("Quantidade de ímpares:", quantidade_impares)
print("Soma dos pares:", soma_pares)
print("Soma dos ímpares:", soma_impares)
