# ============================================================
# Sistema de Desconto Progressivo - Loja Online
# Aluno: Natali
# Atividade: Ag6_DS_I
# ============================================================

def calcular_desconto_compra():
    try:
        # Entrada de dados: solicita o valor total da compra ao usuário
        valor_compra = float(input("Digite o valor total da compra (R$): "))
        
        # Validação para evitar valores zerados ou negativos
        if valor_compra <= 0:
            print("Por favor, informe um valor válido e maior que zero.")
            return

        # Estrutura condicional para determinar o percentual de desconto
        if valor_compra < 200.00:
            percentual_desconto = 0.05  # 5% de desconto
        elif valor_compra < 300.00:
            percentual_desconto = 0.10  # 10% de desconto
        else:
            percentual_desconto = 0.15  # 15% de desconto

        # Processamento: cálculo do valor do desconto e total final a pagar
        valor_desconto = valor_compra * percentual_desconto
        valor_final = valor_compra - valor_desconto

        # Saída de dados: exibição dos resultados formatados
        print("\n--- RESUMO DA COMPRA ---")
        print(f"Valor original da compra: R$ {valor_compra:.2f}")
        print(f"Desconto aplicado ({int(percentual_desconto * 100)}%): R$ {valor_desconto:.2f}")
        print(f"Valor final a pagar: R$ {valor_final:.2f}")

    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números para o valor da compra.")

# Execução do programa
if __name__ == "__main__":
    calcular_desconto_compra()