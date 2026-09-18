# ============================================================
# Calculadora de Consumo Elétrico Inteligente (Recuperação Ag5)
# Aluna: Natali Alves dos Santos Louro
# Atividade: NataliLouro_Rec_Ag5_DS_I
# ============================================================

def calcular_consumo_eletrico():
    print("=== CALCULADORA DE CONSUMO ELÉTRICO INTELIGENTE ===")
    
    # 1. Entrada de dados
    aparelho = input("Digite o nome do aparelho (ex.: Geladeira): ")
    
    try:
        potencia = float(input("Digite a potência do aparelho em Watts (W): "))
        horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))
        
        if potencia <= 0 or horas_dia <= 0:
            print("Por favor, digite valores positivos e maiores que zero.")
            return

        # 2. Cálculo do consumo mensal em kWh
        # Fórmula: consumoMensal = (potencia * horasDia * 30) / 1000
        consumo_mensal = (potencia * horas_dia * 30) / 1000
        
        # Custo estimado (Tarifa fixa de R$ 0,75 por kWh)
        tarifa_kwh = 0.75
        custo_estimado = consumo_mensal * tarifa_kwh

        # 3. Exibição do resultado formatado
        print("\n" + "="*40)
        print("RESUMO DO CONSUMO ESTIMADO")
        print("="*40)
        print(f"Aparelho: {aparelho}")
        print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
        print(f"Custo mensal estimado (R$ 0,75/kWh): R$ {custo_estimado:.2f}")
        print("="*40)

    except ValueError:
        print("Erro: Entrada inválida. Digite apenas números para potência e horas.")

if __name__ == "__main__":
    calcular_consumo_eletrico()