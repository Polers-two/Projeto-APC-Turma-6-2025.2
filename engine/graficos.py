import matplotlib.pyplot as plt


def grafico_completo(resultados):
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