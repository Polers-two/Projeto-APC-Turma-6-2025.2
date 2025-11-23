def calcular_impacto(tempo_execucao, uso_cpu_percent, potencia_cpu=65.0):
    energia = (potencia_cpu * tempo_execucao * (uso_cpu_percent / 100)) / 3600
    co2 = energia * 426
    return {
        "energia_Wh": energia,
        "emissao_CO2_g": co2
    }
