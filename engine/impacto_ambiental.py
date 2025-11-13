# engine/impacto_ambiental.py

def calcular_impacto(tempo_execucao, uso_cpu_percent, potencia_cpu=65):
    """
    Calcula o gasto de energia e emissão de CO2 com base no tempo e uso de CPU.

    Fórmulas:
        E = (P_CPU × T × (uso_cpu% / 100)) / 3600
        CO2 = E × 426

    Parâmetros:
        tempo_execucao: tempo em segundos
        uso_cpu_percent: uso médio da CPU em %
        potencia_cpu: potência média da CPU em watts (padrão 65 W)

    Retorna:
        dict com energia (Wh) e CO2 (g)
    """
    # Energia em Wh
    E = (potencia_cpu * tempo_execucao * (uso_cpu_percent / 100)) / 3600

    # Emissão de CO2 em gramas
    CO2 = E * 426

    return {
        "energia_Wh": E,
        "emissao_CO2_g": CO2
    }
