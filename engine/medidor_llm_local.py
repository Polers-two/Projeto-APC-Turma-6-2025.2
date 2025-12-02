"""
Modulo para medir desempenho de LLMs locais usando Ollama
Compara o impacto de usar LLMs vs algoritmos tradicionais
"""

import subprocess
import psutil
import time
from rich.console import Console
from rich.table import Table
from rich import box
from impacto_ambiental import calcular_impacto

console = Console()


def verificar_ollama():
    """Verifica se o Ollama esta instalado"""
    try:
        resultado = subprocess.run(["ollama", "list"], capture_output=True, text=True, timeout=5)
        return resultado.returncode == 0
    except:
        return False


def listar_modelos():
    """Lista todos os modelos LLM disponiveis no Ollama"""
    try:
        resultado = subprocess.run(["ollama", "list"], capture_output=True, text=True, timeout=5)
        if resultado.returncode == 0:
            linhas = resultado.stdout.strip().split('\n')
            modelos = []
            
            for i in range(1, len(linhas)):
                if linhas[i].strip():
                    partes = linhas[i].split()
                    if partes:
                        modelos.append(partes[0])
            
            return modelos
        return []
    except:
        return []


def executar_query_ollama(modelo, prompt):
    """
    Executa uma query no modelo LLM e mede o desempenho
    """
    processo = psutil.Process()
    processo.cpu_percent()
    tempo_inicio = time.perf_counter()
    
    try:
        comando = ["ollama", "run", modelo, prompt]
        resultado = subprocess.run(comando, capture_output=True, text=True, timeout=120)
        
        tempo_fim = time.perf_counter()
        cpu_percent = processo.cpu_percent()
        tempo_total = tempo_fim - tempo_inicio
        
        if cpu_percent > 100.0:
            cpu_percent = 100.0
        
        if resultado.returncode == 0:
            return {
                "sucesso": True,
                "tempo": tempo_total,
                "cpu": cpu_percent,
                "resposta": resultado.stdout[:500]
            }
        else:
            return {"sucesso": False, "erro": "Erro na execucao"}
    
    except subprocess.TimeoutExpired:
        return {"sucesso": False, "erro": "Timeout (mais de 120s)"}
    except Exception as e:
        return {"sucesso": False, "erro": str(e)}


def medir_llm_local(modelo, lista_original=None, prompt_customizado=None):
    """
    Mede o desempenho de um LLM local ao ordenar uma lista
    """
    if lista_original is not None:
        if len(lista_original) > 100:
            lista_para_prompt = lista_original[:100]
        else:
            lista_para_prompt = lista_original
        
        prompt = f"""Ordene a seguinte lista de numeros em ordem crescente usando Python.
Liste apenas o codigo Python, sem explicacoes.

Lista: {lista_para_prompt}

Retorne apenas o codigo Python que ordena esta lista."""
        
        console.print(f"\n[cyan]Testando {modelo} com lista de {len(lista_original)} elementos...[/cyan]")
        console.print(f"[dim](Enviando os primeiros {len(lista_para_prompt)} elementos no prompt)[/dim]\n")
    
    elif prompt_customizado:
        prompt = prompt_customizado
        console.print(f"\n[cyan]Executando query no modelo {modelo}...[/cyan]")
    
    else:
        prompt = "Escreva um codigo Python simples para ordenar uma lista de numeros."
        console.print(f"\n[cyan]Executando query no modelo {modelo}...[/cyan]")
    
    resultado = executar_query_ollama(modelo, prompt)
    
    if not resultado["sucesso"]:
        console.print(f"[red]Erro: {resultado['erro']}[/red]")
        return None
    
    impacto = calcular_impacto(resultado["tempo"], resultado["cpu"])
    
    console.print(f"[bold]Tempo:[/bold] {resultado['tempo']:.6f}s")
    console.print(f"[bold]CPU:[/bold] {resultado['cpu']:.2f}%")
    console.print(f"[bold]Energia:[/bold] {impacto['energia_Wh']:.6f} Wh")
    console.print(f"[bold]CO2:[/bold] {impacto['emissao_CO2_g']:.4f} g")
    console.print(f"\n[dim]Resposta (primeiros 500 caracteres):[/dim]")
    console.print(f"[dim]{resultado['resposta'][:500]}...[/dim]")
    
    tamanho_lista = len(lista_original) if lista_original else 0
    
    return {
        "modelo": modelo,
        "tempo": resultado["tempo"],
        "cpu": resultado["cpu"],
        "energia": impacto["energia_Wh"],
        "co2": impacto["emissao_CO2_g"],
        "tamanho_lista": tamanho_lista
    }


def comparar_algoritmo_vs_llm(resultado_python, resultado_llm):
    """
    Compara o desempenho de um algoritmo Python com um LLM local
    """
    if not resultado_python or not resultado_llm:
        console.print("[red]Faltam dados para comparacao.[/red]")
        return
    
    if "algoritmo" in resultado_python:
        nome_python = resultado_python["algoritmo"]
    else:
        nome_python = "Python"
    
    if "modelo" in resultado_python and "algoritmo" not in resultado_python:
        console.print("[yellow]Aviso: Voce esta comparando dois LLMs![/yellow]")
        console.print("[yellow]Execute um algoritmo tradicional antes de usar a opcao 11.[/yellow]\n")
    
    tabela = Table(title="Algoritmo Python vs LLM Local", box=box.ROUNDED)
    tabela.add_column("Metodo", style="bold")
    tabela.add_column("Tempo (s)")
    tabela.add_column("CPU (%)")
    tabela.add_column("Energia (Wh)")
    tabela.add_column("CO2 (g)")
    tabela.add_column("Fator", justify="right")
    
    tempo_python = resultado_python["tempo"]
    energia_python = resultado_python["energia"]
    
    tabela.add_row(
        f"[cyan]{nome_python}[/cyan]",
        f"{tempo_python:.6f}",
        f"{resultado_python['cpu']:.2f}",
        f"{energia_python:.6f}",
        f"{resultado_python['co2']:.4f}",
        "[cyan]1.00x[/cyan]"
    )
    
    if tempo_python > 0:
        fator_tempo = resultado_llm["tempo"] / tempo_python
    else:
        fator_tempo = 0
    
    if energia_python > 0:
        fator_energia = resultado_llm["energia"] / energia_python
    else:
        fator_energia = 0
    
    if fator_energia > 100:
        cor = "red"
    elif fator_energia > 10:
        cor = "yellow"
    else:
        cor = "green"
    
    tabela.add_row(
        f"[{cor}]{resultado_llm['modelo']}[/{cor}]",
        f"{resultado_llm['tempo']:.6f}",
        f"{resultado_llm['cpu']:.2f}",
        f"{resultado_llm['energia']:.6f}",
        f"{resultado_llm['co2']:.4f}",
        f"[{cor}]{fator_energia:.1f}x[/{cor}]"
    )
    
    console.print("\n")
    console.print(tabela)
    
    console.print("\n[bold]Analise:[/bold]")
    console.print(f"- O LLM levou {fator_tempo:.1f}x mais tempo")
    console.print(f"- O LLM consumiu {fator_energia:.1f}x mais energia")
       
    if "tamanho_lista" in resultado_llm and resultado_llm["tamanho_lista"] > 0:
        console.print(f"\n[dim]Ambos processaram a mesma lista de {resultado_llm['tamanho_lista']} elementos[/dim]")


def menu_llm_local():
    """
    Mostra menu de selecao de modelos LLM
    """
    if not verificar_ollama():
        console.print("[red]Ollama nao encontrado![/red]")
        console.print("Instale em: https://ollama.ai")
        return None
    
    modelos = listar_modelos()
    
    if not modelos:
        console.print("[red]Nenhum modelo encontrado![/red]")
        console.print("Baixe um modelo com: [cyan]ollama pull llama3.2[/cyan]")
        return None
    
    console.print("\n[bold]Modelos disponiveis:[/bold]")
    for i in range(len(modelos)):
        console.print(f"  {i+1}. {modelos[i]}")
    
    return modelos
