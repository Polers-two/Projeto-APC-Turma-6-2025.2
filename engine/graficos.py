"""
Módulo de geração de gráficos comparativos
Suporta comparação entre Python e outras linguagens (C, Java, Go)
"""

import matplotlib.pyplot as plt
import numpy as np


def grafico_completo(resultados):
    """
    Gera gráfico comparativo apenas com resultados Python
    
    Args:
        resultados: Lista de dicionários com dados de execução Python
    """
    if not resultados:
        print("Sem dados para gerar gráfico.")
        return
    
    algoritmos = [r["algoritmo"] for r in resultados]
    tempos = [r["tempo"] for r in resultados]
    energia = [r["energia"] for r in resultados]
    co2 = [r["co2"] for r in resultados]
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    axes[0].bar(algoritmos, tempos, color="#3498db", edgecolor="black")
    axes[0].set_title("Tempo de Execução", fontweight="bold")
    axes[0].set_ylabel("Segundos")
    axes[0].tick_params(axis="x", rotation=20)
    
    axes[1].bar(algoritmos, energia, color="#2ecc71", edgecolor="black")
    axes[1].set_title("Consumo de Energia", fontweight="bold")
    axes[1].set_ylabel("Wh")
    axes[1].tick_params(axis="x", rotation=20)
    
    axes[2].bar(algoritmos, co2, color="#e74c3c", edgecolor="black")
    axes[2].set_title("Emissão de CO₂", fontweight="bold")
    axes[2].set_ylabel("Gramas")
    axes[2].tick_params(axis="x", rotation=20)
    
    plt.suptitle("Análise Comparativa de Algoritmos de Ordenação", fontsize=14, fontweight="bold")
    plt.tight_layout()
    plt.show()


def grafico_comparativo_linguagens(resultados_python, algoritmo, tamanho):
    """
    Gera gráfico comparativo entre Python e outras linguagens (C, Java, Go)
    
    Args:
        resultados_python: Lista de dicionários com resultados Python
        algoritmo: Nome do algoritmo a comparar
        tamanho: Tamanho da lista testada
    """
    try:
        from comparador_linguagens import obter_todos_benchmarks
    except ImportError:
        print("⚠️  Módulo comparador_linguagens.py não encontrado!")
        print("💡 Certifique-se de que o arquivo está no mesmo diretório.")
        return
    
    # Normalizar nome do algoritmo
    alg_normalizado = algoritmo.lower().replace(" sort", "").replace("sort", "").strip()
    
    # Buscar resultado Python para o algoritmo específico
    resultado_python = None
    for r in resultados_python:
        r_alg_normalizado = r["algoritmo"].lower().replace(" sort", "").replace("sort", "").strip()
        if r_alg_normalizado == alg_normalizado:
            resultado_python = r
            break
    
    if not resultado_python:
        print(f"❌ Nenhum resultado Python encontrado para {algoritmo}")
        return
    
    # Buscar dados de outras linguagens
    outras_linguagens = obter_todos_benchmarks(alg_normalizado, tamanho)
    
    if not outras_linguagens:
        print(f"⚠️  Sem dados de benchmark para {algoritmo} com {tamanho} elementos")
        return
    
    # Preparar dados para o gráfico
    linguagens = ["Python"] + [lang.upper() for lang in outras_linguagens.keys()]
    tempos = [resultado_python["tempo"]] + [dados["tempo"] for dados in outras_linguagens.values()]
    energias = [resultado_python["energia"]] + [dados["energia"] for dados in outras_linguagens.values()]
    co2s = [resultado_python["co2"]] + [dados["co2"] for dados in outras_linguagens.values()]
    
    # Cores para cada linguagem
    cores = {
        "Python": "#3776ab",  # Azul Python
        "C": "#555555",       # Cinza C
        "JAVA": "#f89820",    # Laranja Java
        "GO": "#00add8"       # Ciano Go
    }
    cores_lista = [cores.get(lang, "#cccccc") for lang in linguagens]
    
    # Criar figura com 3 subplots
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    
    # Gráfico 1: Tempo de Execução
    bars1 = axes[0].bar(linguagens, tempos, color=cores_lista, edgecolor="black", linewidth=1.5)
    axes[0].set_title("⏱️ Tempo de Execução", fontweight="bold", fontsize=12)
    axes[0].set_ylabel("Segundos", fontweight="bold")
    axes[0].tick_params(axis="x", rotation=15)
    axes[0].grid(axis='y', alpha=0.3, linestyle='--')
    
    # Adicionar valores nas barras
    for bar in bars1:
        height = bar.get_height()
        axes[0].text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.6f}s',
                    ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    # Gráfico 2: Consumo de Energia
    bars2 = axes[1].bar(linguagens, energias, color=cores_lista, edgecolor="black", linewidth=1.5)
    axes[1].set_title("⚡ Consumo de Energia", fontweight="bold", fontsize=12)
    axes[1].set_ylabel("Wh", fontweight="bold")
    axes[1].tick_params(axis="x", rotation=15)
    axes[1].grid(axis='y', alpha=0.3, linestyle='--')
    
    # Adicionar valores nas barras
    for bar in bars2:
        height = bar.get_height()
        axes[1].text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.6f}',
                    ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    # Gráfico 3: Emissão de CO2
    bars3 = axes[2].bar(linguagens, co2s, color=cores_lista, edgecolor="black", linewidth=1.5)
    axes[2].set_title("🌍 Emissão de CO₂", fontweight="bold", fontsize=12)
    axes[2].set_ylabel("Gramas", fontweight="bold")
    axes[2].tick_params(axis="x", rotation=15)
    axes[2].grid(axis='y', alpha=0.3, linestyle='--')
    
    # Adicionar valores nas barras
    for bar in bars3:
        height = bar.get_height()
        axes[2].text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.4f}g',
                    ha='center', va='bottom', fontsize=9, fontweight='bold')
    
    # Título geral
    plt.suptitle(f"Comparação Multi-Linguagem: {algoritmo.upper()} ({tamanho:,} elementos)", 
                 fontsize=14, fontweight="bold")
    
    plt.tight_layout()
    plt.show()
    
    # Mostrar speedups
    print("\n" + "="*60)
    print(f"📊 SPEEDUP RELATIVO AO PYTHON ({algoritmo.upper()})")
    print("="*60)
    tempo_python = resultado_python["tempo"]
    for i, lang in enumerate(linguagens[1:], 1):
        speedup = tempo_python / tempos[i]
        emoji = "🚀" if speedup > 1 else "🐌"
        print(f"{emoji} {lang:6s}: {speedup:6.2f}x {'mais rápido' if speedup > 1 else 'mais lento'}")
    print("="*60)


def grafico_comparativo_todos_algoritmos(resultados_python, tamanho):
    """
    Gera gráfico comparativo de TODOS os algoritmos entre Python e outras linguagens
    
    Args:
        resultados_python: Lista de dicionários com resultados Python
        tamanho: Tamanho da lista testada
    """
    try:
        from comparador_linguagens import obter_todos_benchmarks, listar_todos_algoritmos
    except ImportError:
        print("⚠️  Módulo comparador_linguagens.py não encontrado!")
        return
    
    algoritmos_disponiveis = listar_todos_algoritmos()
    
    # Filtrar apenas algoritmos que temos em Python (normalizar nomes)
    algoritmos_python = {}
    for r in resultados_python:
        alg_normalizado = r["algoritmo"].lower().replace(" sort", "").replace("sort", "").strip()
        algoritmos_python[alg_normalizado] = r
    
    algoritmos_comuns = [alg for alg in algoritmos_disponiveis if alg in algoritmos_python]
    
    if not algoritmos_comuns:
        print("❌ Nenhum algoritmo comum encontrado entre Python e benchmarks")
        return
    
    # Preparar dados
    linguagens = ["Python", "C", "Java", "Go"]
    dados_tempo = {lang: [] for lang in linguagens}
    
    for alg in algoritmos_comuns:
        # Python
        dados_tempo["Python"].append(algoritmos_python[alg]["tempo"])
        
        # Outras linguagens
        outras = obter_todos_benchmarks(alg, tamanho)
        dados_tempo["C"].append(outras.get("c", {}).get("tempo", 0))
        dados_tempo["Java"].append(outras.get("java", {}).get("tempo", 0))
        dados_tempo["Go"].append(outras.get("go", {}).get("tempo", 0))
    
    # Criar gráfico de barras agrupadas
    x = np.arange(len(algoritmos_comuns))
    width = 0.2
    
    fig, ax = plt.subplots(figsize=(14, 7))
    
    cores = {
        "Python": "#3776ab",
        "C": "#555555",
        "Java": "#f89820",
        "Go": "#00add8"
    }
    
    for i, lang in enumerate(linguagens):
        offset = width * (i - 1.5)
        bars = ax.bar(x + offset, dados_tempo[lang], width, 
                     label=lang, color=cores[lang], edgecolor="black", linewidth=1.2)
        
        # Adicionar valores nas barras (apenas se não for zero)
        for bar in bars:
            height = bar.get_height()
            if height > 0:
                ax.text(bar.get_x() + bar.get_width()/2., height,
                       f'{height:.4f}',
                       ha='center', va='bottom', fontsize=8, rotation=90)
    
    ax.set_xlabel('Algoritmos', fontweight='bold', fontsize=12)
    ax.set_ylabel('Tempo (segundos)', fontweight='bold', fontsize=12)
    ax.set_title(f'Comparação de Performance: Todos os Algoritmos ({tamanho:,} elementos)', 
                fontweight='bold', fontsize=14)
    ax.set_xticks(x)
    ax.set_xticklabels([alg.capitalize() for alg in algoritmos_comuns])
    ax.legend(loc='upper left', fontsize=10)
    ax.grid(axis='y', alpha=0.3, linestyle='--')
    
    plt.tight_layout()
    plt.show()
    
    print("\n✅ Gráfico comparativo gerado com sucesso!")