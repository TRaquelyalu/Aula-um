# Solicita o preço da mercadoria e o percentual de desconto

preco_mercadoria = float(input("Digite o preço da mercadoria: "))
percentual_desconto = float(input("Digite o percentual de desconto: "))

# Calcula o valor do desconto

valor_desconto = preco_mercadoria * (percentual_desconto / 100)

# Calcula o preço final a pagar

preco_final = preco_mercadoria - valor_desconto

# Exibe o valor do desconto e o preço final

print(f"O valor do desconto é: R${valor_desconto:.2f}")
print(f"O preço a pagar é: R${preco_final:.2f}")