"""
Modulo para calcular impacto ambiental de execucoes
Calcula consumo de energia e emissao de CO2
"""


def calcular_impacto(tempo_segundos, uso_cpu_percent, potencia_cpu=65.0):
    """
    Calcula impacto ambiental baseado no tempo e uso de CPU
    
    Formulas:
        Energia (Wh) = (Potencia_CPU * Tempo * Uso_CPU%) / 3600
        CO2 (g) = Energia * 426 gCO2/kWh
    
    Parametros:
        tempo_segundos: Tempo de execucao em segundos
        uso_cpu_percent: Uso da CPU em porcentagem (0-100)
        potencia_cpu: Potencia da CPU em watts (padrao: 65W)
    
    Retorna:
        Dicionario com energia_Wh e emissao_CO2_g
    
    """
    energia = (potencia_cpu * tempo_segundos * (uso_cpu_percent / 100)) / 3600
    co2 = energia * 426
    
    return {
        "energia_Wh": energia,
        "emissao_CO2_g": co2
    }
