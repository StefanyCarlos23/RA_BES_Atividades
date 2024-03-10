"""
6) Calcular preço de venda para produto por quilo.
"""
quantidade = float(input("Qual a quantidade (em kg) do produto?\n"))
preco = float(input("Qual o preço do pruduto em reais?\n"))
print(f"O valor do produto por kg é de R$ {preco/quantidade:.2f}")
