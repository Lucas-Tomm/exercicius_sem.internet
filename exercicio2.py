nome = input("Digite seu nome: ")
ano_nascimento = int(input("Digite seu ano de nascimento: "))
ano_atual = int(input("Digite o ano atual: "))

idade = ano_atual - ano_nascimento

print(nome, "tem", idade, "anos.")

if idade >= 18:
    print("Você já é de maior e pode fazer a carteira de motorista.")
elif idade >= 16:
    print("Você já pode votar.")
else:
    print("Você ainda é menor de idade.")

