import matplotlib.pyplot as plt
import pandas as pd


def plota(metric, ylabel, data):
    ''' Função auxiliar para plotar
     Exemplo de dados
     data = {
         'Algoritmo': ['Bubble Sort', 'Insertion Sort', 'Merge Sort', 'Quick Sort'] * 3,
         'Tamanho': [1000]*4 + [10000]*4 + [1000000]*4,
         'Tempo (s)': [0.05, 0.03, 0.002, 0.0015, 5.4, 3.2, 0.12, 0.08, 650, 430, 12, 9],
         'Energia (Wh)': [0.001, 0.0008, 0.0001, 0.00009, 0.12, 0.08, 0.004, 0.003, 15, 10, 0.5, 0.4],
         'CO2 (g)': [0.3, 0.2, 0.05, 0.04, 35, 25, 1.3, 1.0, 4500, 3000, 120, 100]}
     Exemplos de chamadas
     plota('Tempo (s)', 'Tempo médio (s)', data)
     plota('Energia (Wh)', 'Consumo energético (Wh)', data)
     plota('CO2 (g)', 'Emissão de CO₂ (g)', data)
      '''
    df = pd.DataFrame(data)
    plt.figure(figsize=(8, 5))
    for tamanho in df['Tamanho'].unique():
        subset = df[df['Tamanho'] == tamanho]
        plt.bar(subset['Algoritmo'] + f" ({tamanho})", subset[metric], label=f'{tamanho} itens')
    plt.ylabel(ylabel)
    plt.title(f'Comparação de {ylabel} por Algoritmo e Tamanho da Lista')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()