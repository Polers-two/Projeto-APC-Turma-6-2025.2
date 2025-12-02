"""
Modulo para medir desempenho de funcoes
Mede tempo de execucao e uso de CPU
"""
import psutil
import time


def medir_desempenho(funcao, *args, **kwargs):
    """
    Mede o desempenho de uma funcao
    
    Parametros:
        funcao: A funcao que sera medida
        *args: Argumentos da funcao
        **kwargs: Argumentos nomeados da funcao
    
    Retorna:
        Dicionario com tempo_execucao, uso_cpu_percent e resultado
    """
    processo = psutil.Process()
    processo.cpu_percent()
    
    tempo_inicio = time.perf_counter()
    resultado = funcao(*args, **kwargs)
    tempo_fim = time.perf_counter()
    
    uso_cpu = processo.cpu_percent()
    tempo_total = tempo_fim - tempo_inicio
    
    if uso_cpu > 100.0:
        uso_cpu = 100.0
    
    return {
        "tempo_execucao": tempo_total,
        "uso_cpu_percent": uso_cpu,
        "resultado": resultado
    }
