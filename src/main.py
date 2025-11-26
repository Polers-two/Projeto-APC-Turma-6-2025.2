import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent / "engine"))

from gerador_listas import gerar_listas, mostrar_info_listas
from medidor_desempenho import medir_desempenho
from impacto_ambiental import calcular_impacto
from graficos import (
    grafico_completo,
    grafico_comparativo_linguagens,
    grafico_comparativo_todos_algoritmos,
)
from comparador_linguagens import mostrar_comparacao
from medidor_llm_local import menu_llm_local, medir_llm_local, comparar_algoritmo_vs_llm
from metodos_ordenacao import merge_sort, quick_sort, bubble_sort, insertion_sort, bogosort

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt, InvalidResponse  # InvalidResponse não usado, mas mantido

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
    tabela.add_row("9", "Gráficos Python")
    tabela.add_row("10", "Comparar com outras linguagens (C/Java/Go)")
    tabela.add_row("11", "Medir LLM local (Ollama)")
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

    return {
        "algoritmo": nome,
        "tempo": resultado["tempo_execucao"],
        "cpu": resultado["uso_cpu_percent"],
        "energia": impacto["energia_Wh"],
        "co2": impacto["emissao_CO2_g"],
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
            f"{r['co2']:.4f}",
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
            f"{sum(valores['co2']) / len(valores['co2']):.4f}",
        )
    console.print(tabela)


def main():
    listas = None
    resultados_totais = []

    while True:
        menu()
        opcao = PromptPT.ask(
            "Opção",
            choices=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"],
        )

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

        if opcao == "10":
            if resultados_totais:
                console.print("\n[bold cyan]📊 COMPARAÇÃO COM OUTRAS LINGUAGENS[/bold cyan]")
                console.print("[dim]Escolha o tipo de comparação:[/dim]\n")

                tabela_opcoes = Table(box=box.ROUNDED)
                tabela_opcoes.add_column("Opção", style="bold")
                tabela_opcoes.add_column("Descrição")
                tabela_opcoes.add_row("1", "Comparar um algoritmo específico (Tabela)")
                tabela_opcoes.add_row("2", "Comparar um algoritmo específico (Gráfico)")
                tabela_opcoes.add_row("3", "Comparar todos os algoritmos (Gráfico)")
                console.print(tabela_opcoes)

                sub_opcao = Prompt.ask("\nEscolha", choices=["1", "2", "3"])

                if sub_opcao == "1":
                    # Tabela de comparação
                    algoritmo = Prompt.ask("Qual algoritmo?", choices=["1", "2", "3", "4"])
                    algoritmos_nomes = [
                        "Merge Sort",
                        "Quick Sort",
                        "Bubble Sort",
                        "Insertion Sort",
                    ]
                    nome_alg = algoritmos_nomes[int(algoritmo) - 1]

                    resultado_python = None
                    for r in resultados_totais:
                        if r["algoritmo"] == nome_alg:
                            resultado_python = r
                            break

                    if not resultado_python:
                        console.print(
                            f"[red]Você ainda não executou {nome_alg}. Execute primeiro![/red]"
                        )
                    else:
                        # Perguntar tamanho da lista usada
                        tamanho = IntPrompt.ask("Qual foi o tamanho da lista que você usou?")
                        mostrar_comparacao(resultado_python, nome_alg, tamanho)

                elif sub_opcao == "2":
                    # Gráfico de um algoritmo
                    tamanho = IntPrompt.ask("Qual foi o tamanho da lista que você usou?")
                    algoritmo = Prompt.ask("Qual algoritmo?", choices=["1", "2", "3", "4"])
                    algoritmos_nomes = [
                        "Merge Sort",
                        "Quick Sort",
                        "Bubble Sort",
                        "Insertion Sort",
                    ]
                    nome_alg = algoritmos_nomes[int(algoritmo) - 1]

                    grafico_comparativo_linguagens(resultados_totais, nome_alg, tamanho)

                elif sub_opcao == "3":
                    # Gráfico de todos os algoritmos
                    tamanho = IntPrompt.ask("Qual foi o tamanho da lista que você usou?")
                    grafico_comparativo_todos_algoritmos(resultados_totais, tamanho)
            else:
                console.print("[red]Execute algum algoritmo primeiro (opções 1-4 ou 7).[/red]")
            continue

        if opcao == "11":
            if resultados_totais:
                # Verificar se há lista disponível
                if not listas:
                    console.print(
                        "[red]Gere listas primeiro (opção 6) para comparar com LLM.[/red]"
                    )
                    continue

                # Obter o último resultado Python executado
                resultado_python = resultados_totais[-1]

                # Perguntar qual lista foi usada
                console.print(
                    f"\n[cyan]Último algoritmo executado: {resultado_python['algoritmo']}[/cyan]"
                )
                tamanho = Prompt.ask(
                    "Qual tamanho de lista foi usado?",
                    choices=[str(x) for x in listas.keys()],
                )
                lista_usada = listas[int(tamanho)]

                # Mostrar menu de modelos LLM
                modelos = menu_llm_local()

                if not modelos:
                    continue

                # Escolher modelo
                console.print()
                escolha = IntPrompt.ask(
                    "Escolha o modelo",
                    choices=[str(i) for i in range(1, len(modelos) + 1)],
                )
                modelo_escolhido = modelos[escolha - 1]

                # Medir desempenho do LLM
                resultado_llm = medir_llm_local(modelo_escolhido, lista_usada)

                if resultado_llm:
                    # Comparar resultados
                    comparar_algoritmo_vs_llm(resultado_python, resultado_llm)
            else:
                console.print(
                    "[red]Execute algum algoritmo primeiro (opções 1-5 ou 7).[/red]"
                )
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