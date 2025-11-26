"""
Módulo para cálculo de impacto ambiental de execuções computacionais
Calcula consumo energético e emissões de CO2 baseado em tempo de execução e uso de CPU
"""


def calcular_impacto(tempo_execucao, uso_cpu_percent, potencia_cpu=65.0):
    """
    Calcula o impacto ambiental de uma execução computacional
    
    Fórmulas utilizadas:
    - Energia (Wh) = (Potência_CPU × Tempo × Uso_CPU%) / 3600
    - CO2 (g) = Energia × 426 gCO2/kWh
    
    Fonte da taxa de emissão: IEA (International Energy Agency) 2025
    https://www.iea.org/reports/electricity-2025/emissions
    
    Args:
        tempo_execucao: Tempo de execução em segundos
        uso_cpu_percent: Percentual de uso da CPU (0-100)
        potencia_cpu: Potência média da CPU em watts (padrão: 65W)
    
    Returns:
        Dicionário contendo:
            - energia_Wh: Energia consumida em Watt-hora
            - emissao_CO2_g: Emissão de CO2 em gramas
    """
    # Calcula energia consumida em Wh
    # Divide por 3600 para converter segundos em horas
    energia = (potencia_cpu * tempo_execucao * (uso_cpu_percent / 100)) / 3600
    
    # Calcula emissão de CO2 em gramas
    # 426 gCO2/kWh é a média global de emissões para geração elétrica em 2025
    co2 = energia * 426
    
    return {
        "energia_Wh": energia,
        "emissao_CO2_g": co2
    }