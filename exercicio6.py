nome_mais_velho = ""
idade_mais_velho = 0

for i in range(5):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))

    if idade > idade_mais_velho:
        idade_mais_velho = idade
        nome_mais_velho = nome

print("A pessoa mais velha é:", nome_mais_velho)
print("Idade:", idade_mais_velho)
