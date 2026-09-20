# Programa de Sistema de Desconto Progressivo para Loja Online

# 1. Entrada de dados
# Solicita o valor total da compra ao usuário e converte para número decimal (float)
valor_compra = float(input("Digite o valor total da compra (R$): "))

# 2. Estrutura condicional para determinar a taxa de desconto
# Aplica a regra de negócio baseada no valor acumulado da compra
if valor_compra < 200.00:
    taxa_desconto = 0.05   # 5% de desconto
elif valor_compra < 300.00:
    taxa_desconto = 0.10   # 10% de desconto
else:
    taxa_desconto = 0.15   # 15% de desconto

# 3. Processamento/Cálculos
# Otimizado para calcular o desconto e o valor final sem repetições de código
valor_desconto = valor_compra * taxa_desconto
valor_final = valor_compra - valor_desconto

# 4. Saída de dados
# Exibe os resultados formatados com duas casas decimais
print("\n--- RESUMO DA COMPRA ---")
print(f"Valor original: R$ {valor_compra:.2f}")
print(f"Porcentagem de desconto: {int(taxa_desconto * 100)}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor final a pagar: R$ {valor_final:.2f}")