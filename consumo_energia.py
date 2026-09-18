# ============================================================
# Cálculo de Consumo de Energia Elétrica
# Aluna: Natali Alves dos Santos Louro
# Atividade: Ag5_DS_I
# ============================================================

def calcular_consumo_energia():
    try:
        # Entrada de dados: leitura do consumo em kWh
        consumo_kwh = float(input("Digite o consumo de energia em kWh: "))

        if consumo_kwh <= 0:
            print("Por favor, informe um valor de consumo válido e maior que zero.")
            return

        # Entrada do valor da tarifa por kWh
        tarifa_kwh = float(input("Digite o valor da tarifa por kWh (R$): "))

        if tarifa_kwh <= 0:
            print("Por favor, informe um valor de tarifa válido.")
            return

        # Processamento: cálculo do valor total da conta
        valor_total = consumo_kwh * tarifa_kwh

        # Saída de dados formatada
        print("\n--- RESUMO DO CONSUMO DE ENERGIA ---")
        print(f"Consumo informado: {consumo_kwh:.2f} kWh")
        print(f"Valor da tarifa: R$ {tarifa_kwh:.2f}/kWh")
        print(f"Valor total a pagar: R$ {valor_total:.2f}")

    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números válidos.")

# Execução do programa
if __name__ == "__main__":
    calcular_consumo_energia()