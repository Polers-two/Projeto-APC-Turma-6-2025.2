import psutil
import time


def medir_desempenho(func, *args, **kwargs):
    processo = psutil.Process()
    processo.cpu_percent()
    tempo_inicio = time.perf_counter()
    
    resultado = func(*args, **kwargs)
    
    tempo_fim = time.perf_counter()
    cpu_percent = processo.cpu_percent()
    
    tempo_total = tempo_fim - tempo_inicio
    
    return {
        "tempo_execucao": tempo_total,
        "uso_cpu_percent": min(cpu_percent, 100.0),
        "resultado": resultado
    }