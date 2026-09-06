print("=== Calculadora de Consumo Elétrico Inteligente ===\n")

# Entrada de dados
aparelho = input("Nome do aparelho (ex.: chuveiro): ")
potencia = float(input("Potência do aparelho em Watts (W): "))
horas_dia = float(input("Tempo médio de uso diário em horas: "))

# Cálculo do consumo mensal em kWh
consumo_mensal = (potencia * horas_dia * 30) / 1000

# Cálculo de custo estimado (R$ 0,75 por kWh)
custo_estimado = consumo_mensal * 0.75

# Saída de dados
print("\n--- Resultado ---")
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f}/mês")