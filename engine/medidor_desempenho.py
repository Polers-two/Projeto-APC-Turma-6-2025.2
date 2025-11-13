# engine/medidor_desempenho.py

import psutil
import time

def medir_desempenho(func, *args, **kwargs):
    """
    Mede o tempo e o uso médio de CPU (%) de uma função.

    Parâmetros:
        func: função a ser executada
        *args, **kwargs: argumentos da função

    Retorna:
        dict com tempo (s) e uso médio de CPU (%)
    """
    processo = psutil.Process()
    uso_cpu_inicial = processo.cpu_times()
    tempo_inicial = time.perf_counter()

    # Executa o algoritmo
    resultado = func(*args, **kwargs)

    tempo_final = time.perf_counter()
    uso_cpu_final = processo.cpu_times()

    # Calcula tempo total de execução (s)
    tempo_execucao = tempo_final - tempo_inicial

    # Calcula uso de CPU (user + system)
    tempo_cpu = (uso_cpu_final.user + uso_cpu_final.system) - (
        uso_cpu_inicial.user + uso_cpu_inicial.system
    )

    # % CPU relativa ao tempo total (escala 0–100)
    if tempo_execucao > 0:
        cpu_percentual = (tempo_cpu / tempo_execucao) * 100
    else:
        cpu_percentual = 0.0

    return {
        "tempo_execucao": tempo_execucao,
        "uso_cpu_percent": cpu_percentual,
        "resultado": resultado
    }
