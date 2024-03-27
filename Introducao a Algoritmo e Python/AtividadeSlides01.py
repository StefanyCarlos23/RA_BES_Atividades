#1)Escreva um algoritmo em Python para calcular a idade de alguém,
#sabendo seu ano de nascimento.
anoAtual = 2024
anoNasc = int(input("Qual o ano de nascimento: "))
idade = anoAtual-anoNasc
print(f"Considerando que estamos em {anoAtual}, a idade da pessoa é: {idade} anos.")


##Acabei fazendo diferente, preferi fazer um programa para a pesssoa descobrir quantos anos terá em determinado ano.
print("Olá, este é aplicativo pessoal para descobrir sua idade em anos futuros. Para descobrir sua idade precisamos de alguns dados ")
nome = input("Digite seu nome: ")
anoFut = int(input("Digite o ano que você deseja descobrir a sua idade: "))
anoNasc = int(input ("Digite o ano que você nasceu: "))
idade = anoFut-anoNasc
print(f" {nome} sua idade em {anoFut} será {idade}: ")
