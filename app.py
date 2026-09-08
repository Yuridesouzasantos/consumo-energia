print("⚡ CALCULADORA DE CONSUMO ELÉTRICO ⚡")
print("-" * 40)

aparelho = input("Digite o nome do aparelho: ")
potencia = float(input("Digite a potência do aparelho em watts (W): "))
horas_dia = float(input("Digite o tempo médio de uso diário (horas): "))

consumo_mensal = (potencia * horas_dia * 30) / 1000

valor_kwh = 0.75
custo_estimado = consumo_mensal * valor_kwh

print("\n📊 RESULTADO")
print("-" * 40)
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumo_mensal:.2f} kWh/mês")
print(f"Custo estimado: R$ {custo_estimado:.2f} por mês")
print("-" * 40)
print("💡 Dica: reduzir o tempo de uso pode ajudar a economizar energia!")
