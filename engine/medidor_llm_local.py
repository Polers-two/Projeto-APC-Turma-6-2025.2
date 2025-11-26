"""
Módulo para medição de desempenho de LLMs locais (Ollama)
Compara o impacto ambiental de usar LLMs vs algoritmos tradicionais
"""

import subprocess
import json
import psutil
import time
from rich.console import Console
from rich.table import Table
from rich import box
from impacto_ambiental import calcular_impacto

console = Console()


def verificar_ollama():
    """Verifica se o Ollama está instalado e funcionando"""
    try:
        resultado = subprocess.run(["ollama", "list"], capture_output=True, text=True, timeout=5)
        return resultado.returncode == 0
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return False


def listar_modelos():
    """Lista todos os modelos LLM disponíveis no Ollama"""
    try:
        resultado = subprocess.run(["ollama", "list"], capture_output=True, text=True, timeout=5)
        if resultado.returncode == 0:
            linhas = resultado.stdout.strip().split('\n')[1:]
            modelos = [linha.split()[0] for linha in linhas if linha.strip()]
            return modelos
        return []
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return []


def executar_query_ollama(modelo, prompt):
    """
    Executa uma query no modelo LLM e mede o desempenho
    
    Args:
        modelo: Nome do modelo LLM
        prompt: Texto do prompt a ser enviado
    
    Returns:
        dict: Resultado com tempo, CPU, resposta ou erro
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
        
        if resultado.returncode == 0:
            return {
                "sucesso": True,
                "tempo": tempo_total,
                "cpu": min(cpu_percent, 100.0),
                "resposta": resultado.stdout[:500]  # Aumentado para ver mais da resposta
            }
        else:
            return {"sucesso": False, "erro": "Erro na execução"}
    
    except subprocess.TimeoutExpired:
        return {"sucesso": False, "erro": "Timeout (>120s)"}
    except Exception as e:
        return {"sucesso": False, "erro": str(e)}


def medir_llm_local(modelo, lista_original=None, prompt_customizado=None):
    """
    Mede o desempenho de um LLM local ao ordenar uma lista
    
    Args:
        modelo: Nome do modelo LLM
        lista_original: Lista real que foi usada no algoritmo Python (para comparação justa)
        prompt_customizado: Prompt personalizado (opcional)
    
    Returns:
        dict: Resultados com tempo, CPU, energia, CO2 e tamanho da lista
    """
    # Se uma lista foi fornecida, criar prompt com a lista real
    if lista_original is not None:
        # Limitar o tamanho da lista no prompt para não sobrecarregar
        lista_para_prompt = lista_original[:100] if len(lista_original) > 100 else lista_original
        
        prompt = f"""Ordene a seguinte lista de números em ordem crescente usando Python.
Liste apenas o código Python, sem explicações.

Lista: {lista_para_prompt}

Retorne apenas o código Python que ordena esta lista."""
        
        console.print(f"\n[cyan]Testando {modelo} com lista de {len(lista_original)} elementos...[/cyan]")
        console.print(f"[dim](Enviando os primeiros {len(lista_para_prompt)} elementos no prompt)[/dim]\n")
    
    elif prompt_customizado:
        prompt = prompt_customizado
        console.print(f"\n[cyan]Executando query no modelo {modelo}...[/cyan]")
        console.print(f"[dim]Prompt: {prompt[:100]}...[/dim]\n")
    
    else:
        prompt = "Escreva um código Python simples para ordenar uma lista de números."
        console.print(f"\n[cyan]Executando query no modelo {modelo}...[/cyan]")
        console.print(f"[dim]Prompt padrão[/dim]\n")
    
    resultado = executar_query_ollama(modelo, prompt)
    
    if not resultado["sucesso"]:
        console.print(f"[red]Erro: {resultado['erro']}[/red]")
        return None
    
    impacto = calcular_impacto(resultado["tempo"], resultado["cpu"])
    
    console.print(f"[bold]Tempo:[/bold] {resultado['tempo']:.6f}s")
    console.print(f"[bold]CPU:[/bold] {resultado['cpu']:.2f}%")
    console.print(f"[bold]Energia:[/bold] {impacto['energia_Wh']:.6f} Wh")
    console.print(f"[bold]CO2:[/bold] {impacto['emissao_CO2_g']:.4f} g")
    console.print(f"\n[dim]Resposta (primeiros 500 chars):[/dim]")
    console.print(f"[dim]{resultado['resposta'][:500]}...[/dim]")
    
    return {
        "modelo": modelo,
        "tempo": resultado["tempo"],
        "cpu": resultado["cpu"],
        "energia": impacto["energia_Wh"],
        "co2": impacto["emissao_CO2_g"],
        "tamanho_lista": len(lista_original) if lista_original else 0
    }


def comparar_algoritmo_vs_llm(resultado_python, resultado_llm):
    """
    Compara o desempenho de um algoritmo Python com um LLM local
    
    Args:
        resultado_python: Dicionário com resultados do algoritmo Python
        resultado_llm: Dicionário com resultados do LLM
    """
    if not resultado_python or not resultado_llm:
        console.print("[red]Faltam dados para comparação.[/red]")
        return
    
    # Obter o nome do método Python (pode ser 'algoritmo' ou 'modelo')
    nome_python = resultado_python.get("algoritmo", resultado_python.get("modelo", "Python"))
    
    # Verificar se o resultado_python é realmente um algoritmo tradicional
    if "modelo" in resultado_python and "algoritmo" not in resultado_python:
        console.print("[yellow]⚠️  Aviso: Você está comparando dois LLMs![/yellow]")
        console.print("[yellow]   Execute um algoritmo tradicional (opções 1-5) antes de usar a opção 11.[/yellow]\n")
    
    tabela = Table(title="Algoritmo Python vs LLM Local", box=box.ROUNDED)
    tabela.add_column("Método", style="bold")
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
    
    fator_tempo = resultado_llm["tempo"] / tempo_python if tempo_python > 0 else 0
    fator_energia = resultado_llm["energia"] / energia_python if energia_python > 0 else 0
    cor = "red" if fator_energia > 100 else "yellow" if fator_energia > 10 else "green"
    
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
    
    console.print("\n[bold]Análise:[/bold]")
    console.print(f"• O LLM levou [bold]{fator_tempo:.1f}x mais tempo[/bold]")
    console.print(f"• O LLM consumiu [bold]{fator_energia:.1f}x mais energia[/bold]")
    
    if fator_energia > 100:
        console.print("• [red]Impacto ambiental significativamente maior![/red]")
    elif fator_energia > 10:
        console.print("• [yellow]Impacto ambiental consideravelmente maior[/yellow]")
    else:
        console.print("• [green]Diferença de impacto moderada[/green]")
    
    # Informação adicional sobre a lista
    if resultado_llm.get("tamanho_lista", 0) > 0:
        console.print(f"\n[dim]Ambos processaram a mesma lista de {resultado_llm['tamanho_lista']} elementos[/dim]")


def menu_llm_local():
    """
    Exibe menu de seleção de modelos LLM
    
    Returns:
        list: Lista de modelos disponíveis ou None se Ollama não estiver instalado
    """
    if not verificar_ollama():
        console.print("[red]Ollama não encontrado![/red]")
        console.print("Instale em: https://ollama.ai")
        return None
    
    modelos = listar_modelos()
    
    if not modelos:
        console.print("[red]Nenhum modelo encontrado![/red]")
        console.print("Baixe um modelo com: [cyan]ollama pull llama3.2[/cyan]")
        return None
    
    console.print("\n[bold]Modelos disponíveis:[/bold]")
    for i, modelo in enumerate(modelos, 1):
        console.print(f"  {i}. {modelo}")
    
    return modelos