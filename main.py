"""
Programa principal do Projeto 
Analisa o impacto ambiental de algoritmos de ordenacao
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent / "engine"))

from engine.gerador_listas import gerar_listas, mostrar_info_listas
from engine.medidor_desempenho import medir_desempenho
from engine.impacto_ambiental import calcular_impacto
from engine.graficos import grafico_completo, grafico_comparativo_linguagens, grafico_comparativo_todos_algoritmos
from engine.comparador_linguagens import mostrar_comparacao
from engine.medidor_llm_local import menu_llm_local, medir_llm_local, comparar_algoritmo_vs_llm
from engine.metodos_ordenacao import merge_sort, quick_sort, bubble_sort, insertion_sort, bogosort
from engine.exportador_csv import exportar_resultados, exportar_comparacao_linguagens, exportar_estatisticas

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, IntPrompt
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


class PromptPT(Prompt):
    """Prompt com as mensagens usadas"""
    illegal_choice_message = "[red]Opcao invalida. Escolha uma das opcoes disponiveis.[/red]"


def mostrar_menu():
    """Mostra o menu principal do programa"""
    tabela = Table(title="MENU", box=box.ROUNDED)
    tabela.add_column("Opcao")
    tabela.add_column("Descricao")
    tabela.add_row("1", "Merge Sort")
    tabela.add_row("2", "Quick Sort")
    tabela.add_row("3", "Bubble Sort")
    tabela.add_row("4", "Insertion Sort")
    tabela.add_row("5", "Bogosort (max 10 elementos)")
    tabela.add_row("6", "Gerar listas automaticas")
    tabela.add_row("7", "Comparar todos")
    tabela.add_row("8", "Estatisticas")
    tabela.add_row("9", "Graficos Python")
    tabela.add_row("10", "Comparar com outras linguagens (C/Java/Go)")
    tabela.add_row("11", "Medir LLM local (Ollama)")
    tabela.add_row("12", "Exportar resultados para CSV")
    tabela.add_row("0", "Sair")
    console.print(tabela)


def executar_algoritmo(nome, funcao, lista):
    """
    Executa um algoritmo e mostra os resultados
    """
    if nome == "Bogosort" and len(lista) > 10:
        console.print(Panel("Bogosort so pode ser usado com listas ate 10 elementos.", style="red"))
        return None
    
    resultado = medir_desempenho(funcao, lista[:])
    impacto = calcular_impacto(resultado["tempo_execucao"], resultado["uso_cpu_percent"])
    
    console.print(f"[bold]Tempo:[/bold] {resultado['tempo_execucao']:.6f}s")
    console.print(f"[bold]CPU:[/bold] {resultado['uso_cpu_percent']:.2f}%")
    console.print(f"[bold]Energia:[/bold] {impacto['energia_Wh']:.6f} Wh")
    console.print(f"[bold]CO2:[/bold] {impacto['emissao_CO2_g']:.4f} g")
    
    qtd = IntPrompt.ask("Quantos elementos deseja ver?", default=20)
    lista_resultado = resultado["resultado"][:qtd]
    console.print(Panel(str(lista_resultado), title="Resultado"))
    
    return {
        "algoritmo": nome,
        "tempo": resultado["tempo_execucao"],
        "cpu": resultado["uso_cpu_percent"],
        "energia": impacto["energia_Wh"],
        "co2": impacto["emissao_CO2_g"],
    }


def comparar_todos(lista):
    """
    Executa todos os algoritmos e compara os resultados
    """
    resultados = []
    
    for nome, funcao in ALGORITMOS:
        if nome == "Bogosort" and len(lista) > 10:
            console.print("[yellow]Pulando Bogosort (lista maior que 10).[/yellow]")
            continue
        
        r = executar_algoritmo(nome, funcao, lista)
        if r:
            resultados.append(r)
    
    mostrar_tabela(resultados)
    return resultados


def mostrar_tabela(resultados):
    """
    Mostra uma tabela com os resultados
    """
    tabela = Table(title="Comparacao", box=box.SIMPLE)
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


def calcular_estatisticas(resultados):
    """
    Calcula e mostra estatisticas dos resultados
    """
    if not resultados:
        console.print("[red]Nenhum dado.[/red]")
        return None
    
    stats = {}
    
    for r in resultados:
        if r["algoritmo"] not in stats:
            stats[r["algoritmo"]] = {
                "tempo": [],
                "energia": [],
                "co2": []
            }
        
        stats[r["algoritmo"]]["tempo"].append(r["tempo"])
        stats[r["algoritmo"]]["energia"].append(r["energia"])
        stats[r["algoritmo"]]["co2"].append(r["co2"])
    
    tabela = Table(title="Estatisticas (Medias)", box=box.MINIMAL)
    tabela.add_column("Algoritmo")
    tabela.add_column("Tempo")
    tabela.add_column("Energia")
    tabela.add_column("CO2")
    
    for algoritmo, valores in stats.items():
        tempo_medio = sum(valores['tempo']) / len(valores['tempo'])
        energia_media = sum(valores['energia']) / len(valores['energia'])
        co2_medio = sum(valores['co2']) / len(valores['co2'])
        
        tabela.add_row(
            algoritmo,
            f"{tempo_medio:.6f}",
            f"{energia_media:.6f}",
            f"{co2_medio:.4f}",
        )
    
    console.print(tabela)
    return stats


def menu_exportar_csv(resultados_totais, stats):
    """
    Menu para exportar dados em formato CSV
    """
    if not resultados_totais:
        console.print("[red]Nenhum resultado para exportar. Execute alguns algoritmos primeiro.[/red]")
        return
    
    console.print("\n[bold cyan]EXPORTAR DADOS PARA CSV[/bold cyan]")
    console.print("[dim]Escolha o tipo de exportacao:[/dim]\n")
    
    tabela = Table(box=box.ROUNDED)
    tabela.add_column("Opcao", style="bold")
    tabela.add_column("Descricao")
    tabela.add_row("1", "Exportar todos os resultados")
    tabela.add_row("2", "Exportar estatisticas (medias)")
    tabela.add_row("0", "Voltar")
    console.print(tabela)
    
    opcao = Prompt.ask("\nEscolha", choices=["0", "1", "2"])
    
    if opcao == "0":
        return
    
    if opcao == "1":
        arquivo = exportar_resultados(resultados_totais)
        if arquivo:
            console.print(f"[green]Resultados exportados para: {arquivo}[/green]")
    
    elif opcao == "2":
        if stats:
            arquivo = exportar_estatisticas(stats)
            if arquivo:
                console.print(f"[green]Estatisticas exportadas para: {arquivo}[/green]")
        else:
            console.print("[yellow]Execute a opcao 8 (Estatisticas) antes de exportar.[/yellow]")


def menu_comparacao_linguagens(resultados_totais):
    """
    Menu para comparacao com outras linguagens
    """
    if not resultados_totais:
        console.print("[red]Execute algum algoritmo primeiro (opcoes 1-4 ou 7).[/red]")
        return
    
    console.print("\n[bold cyan]COMPARACAO COM OUTRAS LINGUAGENS[/bold cyan]")
    console.print("[dim]Escolha o tipo de comparacao:[/dim]\n")
    
    tabela_opcoes = Table(box=box.ROUNDED)
    tabela_opcoes.add_column("Opcao", style="bold")
    tabela_opcoes.add_column("Descricao")
    tabela_opcoes.add_row("1", "Comparar um algoritmo especifico (Tabela)")
    tabela_opcoes.add_row("2", "Comparar um algoritmo especifico (Grafico)")
    tabela_opcoes.add_row("3", "Comparar todos os algoritmos (Grafico)")
    console.print(tabela_opcoes)
    
    sub_opcao = Prompt.ask("\nEscolha", choices=["1", "2", "3"])
    
    if sub_opcao == "1":
        algoritmo = Prompt.ask("Qual algoritmo?", choices=["1", "2", "3", "4"])
        algoritmos_nomes = ["Merge Sort", "Quick Sort", "Bubble Sort", "Insertion Sort"]
        nome_alg = algoritmos_nomes[int(algoritmo) - 1]
        
        resultado_python = None
        for r in resultados_totais:
            if r["algoritmo"] == nome_alg:
                resultado_python = r
                break
        
        if not resultado_python:
            console.print(f"[red]Voce ainda nao executou {nome_alg}. Execute primeiro![/red]")
        else:
            tamanho = IntPrompt.ask("Qual foi o tamanho da lista que voce usou?")
            mostrar_comparacao(resultado_python, nome_alg, tamanho)
    
    elif sub_opcao == "2":
        tamanho = IntPrompt.ask("Qual foi o tamanho da lista que voce usou?")
        algoritmo = Prompt.ask("Qual algoritmo?", choices=["1", "2", "3", "4"])
        algoritmos_nomes = ["Merge Sort", "Quick Sort", "Bubble Sort", "Insertion Sort"]
        nome_alg = algoritmos_nomes[int(algoritmo) - 1]
        
        grafico_comparativo_linguagens(resultados_totais, nome_alg, tamanho)
    
    elif sub_opcao == "3":
        tamanho = IntPrompt.ask("Qual foi o tamanho da lista que voce usou?")
        grafico_comparativo_todos_algoritmos(resultados_totais, tamanho)


def menu_llm(resultados_totais, listas):
    """
    Menu para comparacao com LLM
    """
    if not resultados_totais:
        console.print("[red]Execute algum algoritmo primeiro (opcoes 1-5 ou 7).[/red]")
        return
    
    if not listas:
        console.print("[red]Gere listas primeiro (opcao 6) para comparar com LLM.[/red]")
        return
    
    resultado_python = resultados_totais[-1]
    
    console.print(f"\n[cyan]Ultimo algoritmo executado: {resultado_python['algoritmo']}[/cyan]")
    tamanho = Prompt.ask("Qual tamanho de lista foi usado?", choices=[str(x) for x in listas.keys()])
    lista_usada = listas[int(tamanho)]
    
    modelos = menu_llm_local()
    
    if not modelos:
        return
    
    console.print()
    escolha = IntPrompt.ask("Escolha o modelo", choices=[str(i) for i in range(1, len(modelos) + 1)])
    modelo_escolhido = modelos[escolha - 1]
    
    resultado_llm = medir_llm_local(modelo_escolhido, lista_usada)
    
    if resultado_llm:
        comparar_algoritmo_vs_llm(resultado_python, resultado_llm)


def main():
    """
    Funcao principal do programa
    """
    listas = None
    resultados_totais = []
    stats = None
    
    while True:
        mostrar_menu()
        opcao = PromptPT.ask(
            "Opcao",
            choices=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"],
        )
        
        if opcao == "0":
            console.print("[bold green]Programa encerrado.[/bold green]")
            break
        
        if opcao == "6":
            listas = gerar_listas()
            mostrar_info_listas(listas)
            continue
        
        if opcao == "7":
            if listas:
                tamanho = Prompt.ask("Tamanho", choices=[str(x) for x in listas.keys()])
                resultados_totais = resultados_totais + comparar_todos(listas[int(tamanho)])
            else:
                console.print("[red]Gere listas primeiro (opcao 6).[/red]")
            continue
        
        if opcao == "8":
            stats = calcular_estatisticas(resultados_totais)
            continue
        
        if opcao == "9":
            grafico_completo(resultados_totais)
            continue
        
        if opcao == "10":
            menu_comparacao_linguagens(resultados_totais)
            continue
        
        if opcao == "11":
            menu_llm(resultados_totais, listas)
            continue
        
        if opcao == "12":
            menu_exportar_csv(resultados_totais, stats)
            continue
        
        if opcao in ["1", "2", "3", "4", "5"]:
            if listas:
                tamanho = Prompt.ask("Tamanho", choices=[str(x) for x in listas.keys()])
                lista = listas[int(tamanho)]
            else:
                entrada = Prompt.ask("Digite a lista separada por espacos")
                lista = []
                for x in entrada.split():
                    lista.append(int(x))
            
            nome, funcao = ALGORITMOS[int(opcao) - 1]
            r = executar_algoritmo(nome, funcao, lista)
            if r:
                resultados_totais.append(r)


if __name__ == "__main__":
    main()
