"""
Modulo de geracao de graficos comparativos
Cria graficos para comparar algoritmos e linguagens
"""

import matplotlib.pyplot as plt
import numpy as np


def grafico_completo(resultados):
    """
    Gera grafico comparativo com resultados Python
    """
    if not resultados:
        print("Sem dados para gerar grafico.")
        return
    
    algoritmos = []
    tempos = []
    energia = []
    co2 = []
    
    for r in resultados:
        algoritmos.append(r["algoritmo"])
        tempos.append(r["tempo"])
        energia.append(r["energia"])
        co2.append(r["co2"])
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    axes[0].bar(algoritmos, tempos, color="#3498db", edgecolor="black")
    axes[0].set_title("Tempo de Execucao", fontweight="bold")
    axes[0].set_ylabel("Segundos")
    axes[0].tick_params(axis="x", rotation=20)
    
    axes[1].bar(algoritmos, energia, color="#2ecc71", edgecolor="black")
    axes[1].set_title("Consumo de Energia", fontweight="bold")
    axes[1].set_ylabel("Wh")
    axes[1].tick_params(axis="x", rotation=20)
    
    axes[2].bar(algoritmos, co2, color="#e74c3c", edgecolor="black")
    axes[2].set_title("Emissao de CO2", fontweight="bold")
    axes[2].set_ylabel("Gramas")
    axes[2].tick_params(axis="x", rotation=20)
    
    plt.suptitle("Analise Comparativa de Algoritmos de Ordenacao", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()


def grafico_comparativo_linguagens(resultados_python, algoritmo, tamanho):
    """
    Gera grafico comparativo entre Python e outras linguagens
    """
    try:
        from comparador_linguagens import obter_todos_benchmarks
    except ImportError:
        print("Modulo comparador_linguagens.py nao encontrado!")
        return
    
    alg_normalizado = algoritmo.lower().replace(" sort", "").replace("sort", "").strip()
    
    resultado_python = None
    for r in resultados_python:
        r_alg = r["algoritmo"].lower().replace(" sort", "").replace("sort", "").strip()
        if r_alg == alg_normalizado:
            resultado_python = r
            break
    
    if not resultado_python:
        print(f"Nenhum resultado Python encontrado para {algoritmo}")
        return
    
    outras_linguagens = obter_todos_benchmarks(alg_normalizado, tamanho)
    
    if not outras_linguagens:
        print(f"Sem dados de benchmark para {algoritmo} com {tamanho} elementos")
        return
    
    linguagens = ["Python"]
    tempos = [resultado_python["tempo"]]
    energias = [resultado_python["energia"]]
    co2s = [resultado_python["co2"]]
    
    for lang, dados in outras_linguagens.items():
        linguagens.append(lang.upper())
        tempos.append(dados["tempo"])
        energias.append(dados["energia"])
        co2s.append(dados["co2"])
    
    cores = {
        "Python": "#52A736",
        "C": "#555555",
        "JAVA": "#f89820",
        "GO": "#00add8"
    }
    
    cores_lista = []
    for lang in linguagens:
        if lang in cores:
            cores_lista.append(cores[lang])
        else:
            cores_lista.append("#cccccc")
    
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    
    bars1 = axes[0].bar(linguagens, tempos, color=cores_lista, edgecolor="black", linewidth=1.5)
    axes[0].set_title("Tempo de Execucao", fontweight="bold", fontsize=12)
    axes[0].set_ylabel("Segundos", fontweight="bold")
    axes[0].tick_params(axis="x", rotation=15)
    axes[0].grid(axis='y', alpha=0.3, linestyle='--')
    
    for bar in bars1:
        height = bar.get_height()
        axes[0].text(bar.get_x() + bar.get_width()/2., height,
                     f'{height:.6f}s',
                     ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    bars2 = axes[1].bar(linguagens, energias, color=cores_lista, edgecolor="black", linewidth=1.5)
    axes[1].set_title("Consumo de Energia", fontweight="bold", fontsize=12)
    axes[1].set_ylabel("Wh", fontweight="bold")
    axes[1].tick_params(axis="x", rotation=15)
    axes[1].grid(axis='y', alpha=0.3, linestyle='--')
    
    for bar in bars2:
        height = bar.get_height()
        axes[1].text(bar.get_x() + bar.get_width()/2., height,
                     f'{height:.6f}',
                     ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    bars3 = axes[2].bar(linguagens, co2s, color=cores_lista, edgecolor="black", linewidth=1.5)
    axes[2].set_title("Emissao de CO2", fontweight="bold", fontsize=12)
    axes[2].set_ylabel("Gramas", fontweight="bold")
    axes[2].tick_params(axis="x", rotation=15)
    axes[2].grid(axis='y', alpha=0.3, linestyle='--')
    
    for bar in bars3:
        height = bar.get_height()
        axes[2].text(bar.get_x() + bar.get_width()/2., height,
                     f'{height:.4f}g',
                     ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    plt.suptitle(f"Comparacao Multi-Linguagem: {algoritmo.upper()} ({tamanho:,} elementos)", 
                 fontsize=14, fontweight="bold")
    
    plt.tight_layout()
    plt.show()
    
    print("\n" + "="*60)
    print(f"SPEEDUP RELATIVO AO PYTHON ({algoritmo.upper()})")
    print("="*60)
    tempo_python = resultado_python["tempo"]
    for i in range(1, len(linguagens)):
        speedup = tempo_python / tempos[i]
        if speedup > 1:
            print(f"{linguagens[i]:6s}: {speedup:6.2f}x mais rapido")
        else:
            print(f"{linguagens[i]:6s}: {speedup:6.2f}x mais lento")
    print("="*60)


def grafico_comparativo_todos_algoritmos(resultados_python, tamanho):
    """
    Gera grafico comparativo de todos os algoritmos entre Python e outras linguagens
    """
    try:
        from comparador_linguagens import obter_todos_benchmarks, listar_todos_algoritmos
    except ImportError:
        print("Modulo comparador_linguagens.py nao encontrado!")
        return
    
    algoritmos_disponiveis = listar_todos_algoritmos()
    
    algoritmos_python = {}
    for r in resultados_python:
        alg_norm = r["algoritmo"].lower().replace(" sort", "").replace("sort", "").strip()
        algoritmos_python[alg_norm] = r
    
    algoritmos_comuns = []
    for alg in algoritmos_disponiveis:
        if alg in algoritmos_python:
            algoritmos_comuns.append(alg)
    
    if not algoritmos_comuns:
        print("Nenhum algoritmo comum encontrado entre Python e benchmarks")
        return
    
    linguagens = ["Python", "C", "Java", "Go"]
    dados_tempo = {}
    
    for lang in linguagens:
        dados_tempo[lang] = []
    
    for alg in algoritmos_comuns:
        dados_tempo["Python"].append(algoritmos_python[alg]["tempo"])
        
        outras = obter_todos_benchmarks(alg, tamanho)
        
        if "c" in outras:
            dados_tempo["C"].append(outras["c"]["tempo"])
        else:
            dados_tempo["C"].append(0)
        
        if "java" in outras:
            dados_tempo["Java"].append(outras["java"]["tempo"])
        else:
            dados_tempo["Java"].append(0)
        
        if "go" in outras:
            dados_tempo["Go"].append(outras["go"]["tempo"])
        else:
            dados_tempo["Go"].append(0)
    
    x = np.arange(len(algoritmos_comuns))
    width = 0.2
    
    fig, ax = plt.subplots(figsize=(14, 7))
    
    cores = {
        "Python": "#52A736",
        "C": "#555555",
        "Java": "#f89820",
        "Go": "#00add8"
    }
    
    for i in range(len(linguagens)):
        lang = linguagens[i]
        offset = width * (i - 1.5)
        bars = ax.bar(x + offset, dados_tempo[lang], width, 
                      label=lang, color=cores[lang], edgecolor="black", linewidth=1.2)
        
        for bar in bars:
            height = bar.get_height()
            if height > 0:
                ax.text(bar.get_x() + bar.get_width()/2., height,
                        f'{height:.4f}',
                        ha='center', va='bottom', fontsize=8, rotation=90)
    
    ax.set_xlabel('Algoritmos', fontweight='bold', fontsize=12)
    ax.set_ylabel('Tempo (segundos)', fontweight='bold', fontsize=12)
    ax.set_title(f'Comparacao de Performance: Todos os Algoritmos ({tamanho:,} elementos)', 
                 fontweight='bold', fontsize=14)
    ax.set_xticks(x)
    
    labels = []
    for alg in algoritmos_comuns:
        labels.append(alg.capitalize())
    ax.set_xticklabels(labels)
    
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    plt.show()
    
    print("\nGrafico comparativo gerado com sucesso!")
