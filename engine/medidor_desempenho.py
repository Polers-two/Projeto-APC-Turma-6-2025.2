"""
Módulo para medição de desempenho de funções
Mede tempo de execução e uso de CPU
"""
import psutil
import time


def medir_desempenho(func, *args, **kwargs):
    """
    Mede o desempenho de uma função em termos de tempo e uso de CPU
    
    Args:
        func: Função a ser medida
        *args: Argumentos posicionais para a função
        **kwargs: Argumentos nomeados para a função
    
    Returns:
        Dicionário contendo:
            - tempo_execucao: Tempo em segundos
            - uso_cpu_percent: Percentual de uso da CPU
            - resultado: Resultado retornado pela função
    """
    processo = psutil.Process()
    
    # Inicializa medição de CPU (primeira chamada sempre retorna 0.0)
    processo.cpu_percent()
    
    # Marca tempo de início
    tempo_inicio = time.perf_counter()
    
    # Executa a função
    resultado = func(*args, **kwargs)
    
    # Marca tempo de fim
    tempo_fim = time.perf_counter()
    
    # Obtém uso de CPU
    cpu_percent = processo.cpu_percent()
    
    # Calcula tempo total
    tempo_total = tempo_fim - tempo_inicio
    
    return {
        "tempo_execucao": tempo_total,
        "uso_cpu_percent": min(cpu_percent, 100.0),  # Garante que não ultrapasse 100%
        "resultado": resultado
    }