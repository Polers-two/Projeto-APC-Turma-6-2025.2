import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "engine"))

from gerador_listas import gerar_listas, mostrar_info_listas
from medidor_desempenho import medir_desempenho
from impacto_ambiental import calcular_impacto
from graficos import grafico_completo
from metodos_ordenacao import merge_sort, quick_sort, bubble_sort, insertion_sort, bogosort

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt, InvalidResponse


class PromptPT(Prompt):
    illegal_choice_message = "[red]Opção inválida. Escolha uma das opções disponíveis.[/red]"
from rich.panel import Panel
from rich import box

console = Console()

ALGORITMOS = [
    ("Merge Sort", merge_sort),
    ("Quick Sort", quick_sort),
    ("Bubble Sort", bubble_sort),
    ("Insertion Sort", insertion_sort),
    ("Bogosort", bogosort),
]


def menu():
    tabela = Table(title="MENU", box=box.ROUNDED)
    tabela.add_column("Opção")
    tabela.add_column("Descrição")
    tabela.add_row("1", "Merge Sort")
    tabela.add_row("2", "Quick Sort")
    tabela.add_row("3", "Bubble Sort")
    tabela.add_row("4", "Insertion Sort")
    tabela.add_row("5", "Bogosort (máx 10 elementos)")
    tabela.add_row("6", "Gerar listas automáticas")
    tabela.add_row("7", "Comparar todos")
    tabela.add_row("8", "Estatísticas")
    tabela.add_row("9", "Gráficos")
    tabela.add_row("0", "Sair")
    console.print(tabela)


def executar(nome, func, lista):
    if nome == "Bogosort" and len(lista) > 10:
        console.print(Panel("Bogosort só pode ser usado com listas até 10 elementos.", style="red"))
        return None

    resultado = medir_desempenho(func, lista[:])
    impacto = calcular_impacto(resultado["tempo_execucao"], resultado["uso_cpu_percent"])

    console.print(f"[bold]Tempo:[/bold] {resultado['tempo_execucao']:.6f}s")
    console.print(f"[bold]CPU:[/bold] {resultado['uso_cpu_percent']:.2f}%")
    console.print(f"[bold]Energia:[/bold] {impacto['energia_Wh']:.6f} Wh")
    console.print(f"[bold]CO2:[/bold] {impacto['emissao_CO2_g']:.4f} g")

    qtd = IntPrompt.ask("Quantos elementos deseja ver?", default=20)
    console.print(Panel(str(resultado["resultado"][:qtd]), title="Resultado"))
    
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


def comparar(lista):
    resultados = []
    for nome, func in ALGORITMOS:
        if nome == "Bogosort" and len(lista) > 10:
            console.print("[yellow]Pulando Bogosort (lista > 10).[/yellow]")
            continue
        r = executar(nome, func, lista)
        if r:
            resultados.append(r)
    mostrar_tabela(resultados)
    return resultados


def mostrar_tabela(resultados):
    tabela = Table(title="Comparação", box=box.SIMPLE)
    tabela.add_column("Algoritmo")
    tabela.add_column("Tempo")
    tabela.add_column("CPU")
    tabela.add_column("Energia")
    tabela.add_column("CO2")
    for r in resultados:
        tabela.add_row(
            r["algoritmo"],
            f"{r['tempo']:.6f}",
            f"{r['cpu']:.2f}",
            f"{r['energia']:.6f}",
            f"{r['co2']:.4f}"
        )
    console.print(tabela)


def estatisticas(resultados):
    if not resultados:
        console.print("[red]Nenhum dado.[/red]")
        return
    
    stats = {}
    for r in resultados:
        if r["algoritmo"] not in stats:
            stats[r["algoritmo"]] = {"tempo": [], "energia": [], "co2": []}
        stats[r["algoritmo"]]["tempo"].append(r["tempo"])
        stats[r["algoritmo"]]["energia"].append(r["energia"])
        stats[r["algoritmo"]]["co2"].append(r["co2"])
    
    tabela = Table(title="Estatísticas (Médias)", box=box.MINIMAL)
    tabela.add_column("Algoritmo")
    tabela.add_column("Tempo")
    tabela.add_column("Energia")
    tabela.add_column("CO2")
    
    for alg, valores in stats.items():
        tabela.add_row(
            alg,
            f"{sum(valores['tempo']) / len(valores['tempo']):.6f}",
            f"{sum(valores['energia']) / len(valores['energia']):.6f}",
            f"{sum(valores['co2']) / len(valores['co2']):.4f}"
        )
    console.print(tabela)


def main():
    listas = None
    resultados_totais = []
    
    while True:
        menu()
        opcao = PromptPT.ask("Opção", choices=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"])
        
        if opcao == "0":
            break
        
        if opcao == "6":
            listas = gerar_listas()
            mostrar_info_listas(listas)
            continue
        
        if opcao == "7":
            if listas:
                tamanho = Prompt.ask("Tamanho", choices=[str(x) for x in listas.keys()])
                resultados_totais += comparar(listas[int(tamanho)])
            else:
                console.print("[red]Gere listas primeiro (opção 6).[/red]")
            continue
        
        if opcao == "8":
            estatisticas(resultados_totais)
            continue
        
        if opcao == "9":
            grafico_completo(resultados_totais)
            continue
        
        if opcao in ["1", "2", "3", "4", "5"]:
            if listas:
                tamanho = Prompt.ask("Tamanho", choices=[str(x) for x in listas.keys()])
                lista = listas[int(tamanho)]
            else:
                entrada = Prompt.ask("Digite a lista separada por espaços")
                lista = [int(x) for x in entrada.split()]
            
            nome, func = ALGORITMOS[int(opcao) - 1]
            r = executar(nome, func, lista)
            if r:
                resultados_totais.append(r)


if __name__ == "__main__":
    main()