"""
2)Calcular o valor em reais na locadora de carros, sendo que o aluguel
é de 100 reais a diária
"""
tarifa = 100
dias = int(input("Quantos dias o cliente ficará com o carro?\n"))
print(f"O valor total gasto será: R${dias*tarifa},00")


print("Olá, este é o lugar certo para você alugar seu carro. ")
nome = input("Digite seu nome: " )
um = 100
dois = 200
tres = 300
print(f"Diária dos modelos disponíveis: \n Modelo 1: {um:.2f} \n Modelo 2: {dois:.2f} \n Modelo 3: {tres:.2f}")
print(input("Digite o moledo do carro que você deseja: "))
if um:
    print("Você selecionou o modelo 1, agora precisamos saber quantos dias irá alugar o carro")
    dias = int(input("Quantos dias você ficará com o carro?"))
    print(f"O valor total gasto será: R${dias*um},00")
elif dois:
    print("Você selecionou o modelo 2, agora precisamos saber quantos dias irá alugar o carro")
    dias = int(input("Quantos dias você ficará com o carro?"))
    print(f"O valor total gasto será: R${dias*dois},00")
else:
    print("Você selecionou o modelo 3, agora precisamos saber quantos dias irá alugar o carro")
    dias = int(input("Quantos dias você ficará com o carro?"))
    print(f"{nome} O valor total gasto será: R${dias*tres},00")
