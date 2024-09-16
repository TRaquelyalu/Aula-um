# Solicita o valor do salário e a porcentagem de aumento

salario = float(input("Digite o valor do salário atual: "))
porcentagem_aumento = float(input("Digite a porcentagem de aumento: "))

# Calcula o valor do aumento
valor_aumento = salario * (porcentagem_aumento / 100)

# Calcula o novo salário
novo_salario = salario + valor_aumento

# Exibe o valor do aumento e o novo salário
print(f"O valor do aumento é: R${valor_aumento:.2f}")
print(f"O novo salário é: R${novo_salario:.2f}")
