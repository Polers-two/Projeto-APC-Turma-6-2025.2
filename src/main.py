# src/main.py

import sys
import os

# Garante que o Python enxergue a pasta raiz (onde está "engine/")
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from engine.metodos_ordenacao import (
    bubble_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
)
from engine.gerador_listas import gerar_listas, mostrar_info_listas
from engine.medidor_desempenho import medir_desempenho
from engine.impacto_ambiental import calcular_impacto
from engine.gera_plot import plota


# ==================== FUNÇÕES PRINCIPAIS ====================

def exibir_menu():
    print("\n=== MENU DE ALGORITMOS DE ORDENAÇÃO ===")
    print("1 - Merge Sort")
    print("2 - Quick Sort")
    print("3 - Bubble Sort")
    print("4 - Insertion Sort")
    print("5 - Gerar listas automáticas")
    print("6 - Sair")
    print("7 - Comparar todos os algoritmos automaticamente")
    print("8 - Mostrar estatísticas médias e ranking")
    print("========================================")


def executar_algoritmo(nome, funcao, lista, potencia_cpu=65):
    """Executa o algoritmo, mede desempenho e calcula impacto ambiental."""
    resultado = medir_desempenho(funcao, lista.copy())
    impacto = calcular_impacto(
        resultado["tempo_execucao"],
        resultado["uso_cpu_percent"],
        potencia_cpu
    )

    print(f"\n=== {nome} ===")
    print(f"Tempo de execução: {resultado['tempo_execucao']:.4f} s")
    print(f"Uso médio de CPU: {resultado['uso_cpu_percent']:.2f}%")
    print(f"Consumo de energia: {impacto['energia_Wh']:.6f} Wh")
    print(f"Emissão de CO₂: {impacto['emissao_CO2_g']:.4f} g")

    try:
        qtd = int(input("Quantos elementos da lista ordenada você quer visualizar? "))
        if qtd <= 0:
            qtd = 20
    except ValueError:
        qtd = 20

    print(f"Mostrando os {qtd} primeiros elementos ordenados:")
    print(resultado["resultado"][:qtd])

    return {
        "algoritmo": nome,
        "tempo": resultado["tempo_execucao"],
        "cpu": resultado["uso_cpu_percent"],
        "energia": impacto["energia_Wh"],
        "co2": impacto["emissao_CO2_g"]
    }


def comparar_algoritmos(listas_geradas, potencia_cpu=65):
    """Compara todos os algoritmos automaticamente usando a mesma lista."""
    if not listas_geradas:
        print("Nenhuma lista gerada. Gere as listas primeiro (opção 5).")
        return []

    print("\nListas disponíveis:")
    for tamanho in listas_geradas.keys():
        print(f"- {tamanho}")

    try:
        escolha = int(input("Escolha o tamanho da lista para os testes: "))
        lista = listas_geradas.get(escolha)
        if lista is None:
            print("Tamanho inválido.")
            return []
    except ValueError:
        print("Entrada inválida.")
        return []

    print(f"\nIniciando comparação com lista de {len(lista)} elementos...")
    algoritmos = [
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
        ("Bubble Sort", bubble_sort),
        ("Insertion Sort", insertion_sort)
    ]

    resultados = []
    for nome, funcao in algoritmos:
        print(f"\n>>> Testando {nome}...")
        resultados.append(executar_algoritmo(nome, funcao, lista, potencia_cpu))

# geração de plots

    data = {
        'Algoritmo': [algoritmo[0] for algoritmo in algoritmos],
        'Tamanho': [escolha]*4,
        'Tempo (s)': [resultados[i]['tempo'] for i in range(len(resultados))],
        'CPU (%)': [resultados[i]['cpu'] for i in range(len(resultados))],
        'Energia (Wh)': [resultados[i]['energia'] for i in range(len(resultados))],
        'CO2 (g)': [resultados[i]['co2'] for i in range(len(resultados))]
    }

    plota('Tempo (s)', 'Tempo de execução (s)', data)
    plota('CPU (%)', 'Uso de CPU em %', data)
    plota('Energia (Wh)', 'Consumo energético (Wh)', data)
    plota('CO2 (g)', 'Emissão de CO₂ (g)', data)

    print("\n=== COMPARATIVO FINAL ===")
    print(f"{'Algoritmo':<15}{'Tempo (s)':<12}{'CPU (%)':<10}{'Energia (Wh)':<15}{'CO₂ (g)':<10}")
    print("-" * 65)
    for r in resultados:
        print(f"{r['algoritmo']:<15}{r['tempo']:<12.4f}{r['cpu']:<10.2f}{r['energia']:<15.6f}{r['co2']:<10.4f}")
    print("-" * 65)

    return resultados


def mostrar_estatisticas(resultados):
    """Gera médias e ranking a partir da lista de resultados."""
    if not resultados:
        print("\nNenhum resultado disponível ainda.")
        return

    print("\n=== ESTATÍSTICAS GERAIS ===")

    # Média de tempo, CPU, energia e CO₂ por algoritmo
    estatisticas = {}
    for r in resultados:
        nome = r["algoritmo"]
        if nome not in estatisticas:
            estatisticas[nome] = {"tempo": [], "cpu": [], "energia": [], "co2": []}
        estatisticas[nome]["tempo"].append(r["tempo"])
        estatisticas[nome]["cpu"].append(r["cpu"])
        estatisticas[nome]["energia"].append(r["energia"])
        estatisticas[nome]["co2"].append(r["co2"])

    print(f"{'Algoritmo':<15}{'Tempo médio (s)':<18}{'Energia (Wh)':<15}{'CO₂ (g)':<10}")
    print("-" * 60)

    medias = []
    for nome, dados in estatisticas.items():
        tempo_m = sum(dados["tempo"]) / len(dados["tempo"])
        energia_m = sum(dados["energia"]) / len(dados["energia"])
        co2_m = sum(dados["co2"]) / len(dados["co2"])
        medias.append((nome, tempo_m, energia_m, co2_m))
        print(f"{nome:<15}{tempo_m:<18.6f}{energia_m:<15.6f}{co2_m:<10.4f}")

    # Ranking de eficiência (menor tempo)
    ranking = sorted(medias, key=lambda x: x[1])
    print("\n Ranking de eficiência (menor tempo):")
    for i, (nome, tempo, energia, co2) in enumerate(ranking, start=1):
        print(f"{i}. {nome} - {tempo:.6f} s, {energia:.6f} Wh, {co2:.4f} g")


def menu_principal():
    listas_geradas = None
    resultados_totais = []

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "6":
            print("Saindo do programa... Até mais!")
            break

        elif opcao == "5":
            listas_geradas = gerar_listas()
            mostrar_info_listas(listas_geradas)

        elif opcao == "7":
            novos_resultados = comparar_algoritmos(listas_geradas)
            resultados_totais.extend(novos_resultados)

        elif opcao == "8":
            mostrar_estatisticas(resultados_totais)

        else:
            if listas_geradas:
                print("\nListas disponíveis:")
                for tamanho in listas_geradas.keys():
                    print(f"- {tamanho}")
                try:
                    escolha = int(input("Escolha o tamanho da lista para ordenar: "))
                    lista = listas_geradas.get(escolha)
                    if lista is None:
                        print("Tamanho inválido.")
                        continue
                except ValueError:
                    print("Entrada inválida, tente novamente.")
                    continue
            else:
                lista = input("Digite os números separados por espaço: ").split()
                lista = [int(x) for x in lista]

            if opcao == "1":
                resultados_totais.append(executar_algoritmo("Merge Sort", merge_sort, lista))
            elif opcao == "2":
                resultados_totais.append(executar_algoritmo("Quick Sort", quick_sort, lista))
            elif opcao == "3":
                resultados_totais.append(executar_algoritmo("Bubble Sort", bubble_sort, lista))
            elif opcao == "4":
                resultados_totais.append(executar_algoritmo("Insertion Sort", insertion_sort, lista))
            else:
                print("Opção inválida! Tente novamente.")



if __name__ == "__main__":
    menu_principal()
