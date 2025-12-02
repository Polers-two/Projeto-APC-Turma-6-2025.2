"""
Modulo para exportar resultados em formato CSV
Salva dados de benchmarks e comparacoes
"""
import csv
import os
from datetime import datetime


def exportar_resultados(resultados, nome_arquivo=None):
    """
    Exporta lista de resultados para arquivo CSV
    
    Parametros:
        resultados: Lista de dicionarios com dados dos testes
        nome_arquivo: Nome do arquivo (opcional)
    
    Retorna:
        Nome do arquivo criado
    """
    if not resultados:
        return None
    
    if nome_arquivo is None:
        data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo = f"resultados_{data_hora}.csv"
    
    if not nome_arquivo.endswith(".csv"):
        nome_arquivo = nome_arquivo + ".csv"
    
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo:
        colunas = ["algoritmo", "tempo", "cpu", "energia", "co2"]
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)
        
        escritor.writeheader()
        
        for resultado in resultados:
            linha = {}
            for coluna in colunas:
                if coluna in resultado:
                    linha[coluna] = resultado[coluna]
                else:
                    linha[coluna] = ""
            escritor.writerow(linha)
    
    return nome_arquivo


def exportar_comparacao_linguagens(dados, algoritmo, tamanho, nome_arquivo=None):
    """
    Exporta comparacao entre linguagens para CSV
    
    Parametros:
        dados: Dicionario com dados de cada linguagem
        algoritmo: Nome do algoritmo
        tamanho: Tamanho da lista testada
        nome_arquivo: Nome do arquivo (opcional)
    """
    if nome_arquivo is None:
        data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo = f"comparacao_{algoritmo}_{tamanho}_{data_hora}.csv"
    
    if not nome_arquivo.endswith(".csv"):
        nome_arquivo = nome_arquivo + ".csv"
    
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo:
        colunas = ["linguagem", "algoritmo", "tamanho", "tempo", "cpu", "energia", "co2"]
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)
        
        escritor.writeheader()
        
        for linguagem, valores in dados.items():
            linha = {
                "linguagem": linguagem,
                "algoritmo": algoritmo,
                "tamanho": tamanho,
                "tempo": valores.get("tempo", ""),
                "cpu": valores.get("cpu", ""),
                "energia": valores.get("energia", ""),
                "co2": valores.get("co2", "")
            }
            escritor.writerow(linha)
    
    return nome_arquivo


def exportar_estatisticas(estatisticas, nome_arquivo=None):
    """
    Exporta estatisticas agregadas para CSV
    
    Parametros:
        estatisticas: Dicionario com estatisticas por algoritmo
        nome_arquivo: Nome do arquivo (opcional)
    """
    if not estatisticas:
        return None
    
    if nome_arquivo is None:
        data_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
        nome_arquivo = f"estatisticas_{data_hora}.csv"
    
    if not nome_arquivo.endswith(".csv"):
        nome_arquivo = nome_arquivo + ".csv"
    
    with open(nome_arquivo, 'w', newline='', encoding='utf-8') as arquivo:
        colunas = ["algoritmo", "tempo_medio", "energia_media", "co2_medio", "execucoes"]
        escritor = csv.DictWriter(arquivo, fieldnames=colunas)
        
        escritor.writeheader()
        
        for algoritmo, valores in estatisticas.items():
            tempo_medio = sum(valores["tempo"]) / len(valores["tempo"])
            energia_media = sum(valores["energia"]) / len(valores["energia"])
            co2_medio = sum(valores["co2"]) / len(valores["co2"])
            
            linha = {
                "algoritmo": algoritmo,
                "tempo_medio": tempo_medio,
                "energia_media": energia_media,
                "co2_medio": co2_medio,
                "execucoes": len(valores["tempo"])
            }
            escritor.writerow(linha)
    
    return nome_arquivo
