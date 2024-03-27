"""
4)Média de 4 notas
"""
nota1 = float(input("Informe a primeira nota:\n"))
nota2 = float(input("Informe a segunda nota:\n"))
nota3 = float(input("Informe a terceira nota:\n"))
nota4 = float(input("Informe a quarta nota:\n"))
media = (nota1+nota2+nota3+nota4)/4
print(f"A média das 4 notas é: {media:.2f}")

## Decidi usar o while para fazer a média de notas como forma de praticar.
cont = 1
numeroNotas = 4
soma = 0

while cont <=numeroNotas:
    nota = float(input(f"Digite a nota {cont}: "))
    soma += nota
    cont = cont +1
print(f"Sua nota é {soma/numeroNotas:.2f}")
