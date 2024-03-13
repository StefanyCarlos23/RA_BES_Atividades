#Entrada para o aluno digitar a média
media = float(input("Informe sua média: "))
if media>=7:
    print("Aprovado!")
elif media >=4 and media < 7:
    print("Exame final")
    diferenca = 7-media
    print(f"Em exame por {diferenca:.2f} pontos.")
else:
    print("Reprovado!")


