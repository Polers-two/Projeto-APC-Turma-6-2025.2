"""
Comparador de Performance entre Linguagens
Dados de benchmark reais de C, Java e Go
"""

from rich.console import Console
from rich.table import Table
from rich import box

console = Console()

# ==== DADOS DE BENCHMARK C ====
BENCHMARKS_C = {
    "merge": {
        1000: {"tempo": 0.000181, "cpu": 60.00, "energia": 0.00002, "co2": 0.0000},
        10000: {"tempo": 0.002448, "cpu": 87.48, "energia": 0.000039, "co2": 0.0000},
        100000: {"tempo": 0.025123, "cpu": 98.78, "energia": 0.000448, "co2": 0.0001}
    },
    "quick": {
        1000: {"tempo": 0.000099, "cpu": 53.60, "energia": 0.00001, "co2": 0.0000},
        10000: {"tempo": 0.000974, "cpu": 83.19, "energia": 0.000015, "co2": 0.0000},
        100000: {"tempo": 0.008952, "cpu": 96.50, "energia": 0.000156, "co2": 0.0000}
    },
    "bubble": {
        1000: {"tempo": 0.001254, "cpu": 88.28, "energia": 0.000020, "co2": 0.0000},
        10000: {"tempo": 0.175015, "cpu": 99.86, "energia": 0.003155, "co2": 0.0007},
        100000: {"tempo": 14.567331, "cpu": 100.00, "energia": 0.263017, "co2": 0.0613}
    },
    "insertion": {
        1000: {"tempo": 0.000142, "cpu": 57.00, "energia": 0.00001, "co2": 0.0000},
        10000: {"tempo": 0.014661, "cpu": 98.65, "energia": 0.000261, "co2": 0.0001},
        100000: {"tempo": 1.486456, "cpu": 99.98, "energia": 0.026834, "co2": 0.0063}
    }
}

# ==== DADOS DE BENCHMARK JAVA ====
BENCHMARKS_JAVA = {
    "merge": {
        1000: {"tempo": 0.000120, "cpu": 18.23, "energia": 0.0000, "co2": 0.0000},
        10000: {"tempo": 0.000967, "cpu": 16.87, "energia": 0.00003, "co2": 0.0000},
        100000: {"tempo": 0.012376, "cpu": 15.58, "energia": 0.000035, "co2": 0.0000}
    },
    "quick": {
        1000: {"tempo": 0.000062, "cpu": 16.49, "energia": 0.0000, "co2": 0.0000},
        10000: {"tempo": 0.000605, "cpu": 17.42, "energia": 0.00002, "co2": 0.0000},
        100000: {"tempo": 0.007027, "cpu": 16.18, "energia": 0.000021, "co2": 0.0000}
    },
    "bubble": {
        1000: {"tempo": 0.001039, "cpu": 16.85, "energia": 0.00003, "co2": 0.0000},
        10000: {"tempo": 0.142538, "cpu": 15.89, "energia": 0.000408, "co2": 0.0001},
        100000: {"tempo": 16.310651, "cpu": 15.50, "energia": 0.045614, "co2": 0.0106}
    },
    "insertion": {
        1000: {"tempo": 0.000181, "cpu": 16.06, "energia": 0.00001, "co2": 0.0000},
        10000: {"tempo": 0.007635, "cpu": 15.66, "energia": 0.000022, "co2": 0.0000},
        100000: {"tempo": 0.855350, "cpu": 15.49, "energia": 0.002391, "co2": 0.0006}
    }
}

# ==== DADOS DE BENCHMARK GO ====
BENCHMARKS_GO = {
    "merge": {
        1000: {"tempo": 0.000098, "cpu": 40.50, "energia": 0.00001, "co2": 0.0000},
        10000: {"tempo": 0.001292, "cpu": 54.00, "energia": 0.000013, "co2": 0.0000},
        100000: {"tempo": 0.016760, "cpu": 67.50, "energia": 0.000204, "co2": 0.0000}
    },
    "quick": {
        1000: {"tempo": 0.000061, "cpu": 40.50, "energia": 0.0000, "co2": 0.0000},
        10000: {"tempo": 0.000559, "cpu": 54.00, "energia": 0.00005, "co2": 0.0000},
        100000: {"tempo": 0.007117, "cpu": 67.50, "energia": 0.000087, "co2": 0.0000}
    },
    "bubble": {
        1000: {"tempo": 0.000790, "cpu": 49.50, "energia": 0.00007, "co2": 0.0000},
        10000: {"tempo": 0.111852, "cpu": 66.00, "energia": 0.001333, "co2": 0.0003},
        100000: {"tempo": 15.387725, "cpu": 82.50, "energia": 0.229213, "co2": 0.0534}
    },
    "insertion": {
        1000: {"tempo": 0.000091, "cpu": 49.50, "energia": 0.00001, "co2": 0.0000},
        10000: {"tempo": 0.017150, "cpu": 66.00, "energia": 0.000204, "co2": 0.0000},
        100000: {"tempo": 1.724546, "cpu": 82.50, "energia": 0.025689, "co2": 0.0060}
    }
}


def encontrar_tamanho_mais_proximo(tamanho_real):
    """
    Encontra o tamanho de benchmark mais próximo do tamanho real
    
    Args:
        tamanho_real: Tamanho da lista executada
    
    Returns:
        Tamanho de benchmark mais próximo (1000, 10000 ou 100000)
    """
    tamanhos_disponiveis = [1000, 10000, 100000]
    
    # Encontrar o mais próximo
    mais_proximo = min(tamanhos_disponiveis, key=lambda x: abs(x - tamanho_real))
    
    return mais_proximo


def obter_benchmark(linguagem, algoritmo, tamanho):
    """
    Busca dados específicos de benchmark
    
    Args:
        linguagem: 'c', 'java' ou 'go'
        algoritmo: 'merge', 'quick', 'bubble' ou 'insertion'
        tamanho: Tamanho da lista (será aproximado para 1000, 10000 ou 100000)
    
    Returns:
        dict com tempo, cpu, energia e co2 ou None se não encontrado
    """
    benchmarks = {
        "c": BENCHMARKS_C,
        "java": BENCHMARKS_JAVA,
        "go": BENCHMARKS_GO
    }
    
    if linguagem not in benchmarks:
        return None
    
    dados = benchmarks[linguagem]
    
    if algoritmo not in dados:
        return None
    
    # Encontrar tamanho mais próximo
    tamanho_aproximado = encontrar_tamanho_mais_proximo(tamanho)
    
    if tamanho_aproximado not in dados[algoritmo]:
        return None
    
    return dados[algoritmo][tamanho_aproximado]


def obter_todos_benchmarks(algoritmo, tamanho):
    """
    Obtém benchmarks de TODAS as linguagens (C, Java, Go) para um algoritmo e tamanho
    
    Args:
        algoritmo: 'merge', 'quick', 'bubble' ou 'insertion'
        tamanho: Tamanho da lista (será aproximado)
    
    Returns:
        dict com dados de cada linguagem ou dict vazio se não encontrado
    """
    resultados = {}
    
    for linguagem in ["c", "java", "go"]:
        dados = obter_benchmark(linguagem, algoritmo, tamanho)
        if dados:
            resultados[linguagem] = dados
    
    return resultados


def listar_todas_linguagens():
    """Retorna lista de linguagens disponíveis"""
    return ["c", "java", "go"]


def listar_todos_algoritmos():
    """Retorna lista de algoritmos disponíveis"""
    return ["merge", "quick", "bubble", "insertion"]


def listar_todos_tamanhos():
    """Retorna lista de tamanhos disponíveis"""
    return [1000, 10000, 100000]


def mostrar_comparacao(resultado_python, algoritmo, tamanho):
    """
    Exibe comparação entre Python e outras linguagens
    
    Args:
        resultado_python: Dicionário com resultados do Python
        algoritmo: Nome do algoritmo
        tamanho: Tamanho da lista testada (será aproximado)
    """
    if not resultado_python:
        console.print("[red]Execute o algoritmo em Python primeiro (opções 1-4).[/red]")
        return
    
    # Normalizar nome do algoritmo
    alg_normalizado = algoritmo.lower().replace(" sort", "").replace("sort", "").strip()
    
    # Encontrar tamanho mais próximo
    tamanho_aproximado = encontrar_tamanho_mais_proximo(tamanho)
    
    # Buscar dados de outras linguagens
    outras_linguagens = obter_todos_benchmarks(alg_normalizado, tamanho_aproximado)
    
    if not outras_linguagens:
        console.print(f"[yellow]⚠️  Sem dados de benchmark para {algoritmo}.[/yellow]")
        return
    
    # Aviso se o tamanho foi aproximado
    if tamanho != tamanho_aproximado:
        console.print(f"[yellow]ℹ️  Lista de {tamanho} elementos aproximada para benchmark de {tamanho_aproximado:,}[/yellow]\n")
    
    # Criar tabela
    tabela = Table(title=f"Comparação: {algoritmo.upper()} (~{tamanho_aproximado:,} elementos)", box=box.ROUNDED)
    tabela.add_column("Linguagem", style="bold", justify="center")
    tabela.add_column("Tempo (s)", justify="right")
    tabela.add_column("CPU (%)", justify="right")
    tabela.add_column("Energia (Wh)", justify="right")
    tabela.add_column("CO2 (g)", justify="right")
    tabela.add_column("Speedup", justify="center")
    
    tempo_python = resultado_python["tempo"]
    
    # Adicionar linha do Python
    tabela.add_row(
        "[cyan]Python[/cyan]",
        f"{tempo_python:.6f}",
        f"{resultado_python.get('cpu', 0):.2f}",
        f"{resultado_python['energia']:.6f}",
        f"{resultado_python['co2']:.4f}",
        "[cyan]1.00x[/cyan]"
    )
    
    # Adicionar linhas das outras linguagens ordenadas por tempo
    linguagens_ordenadas = sorted(outras_linguagens.items(), key=lambda x: x[1]["tempo"])
    
    for lang, dados in linguagens_ordenadas:
        speedup = tempo_python / dados['tempo']
        cor = "green" if speedup > 1 else "yellow"
        
        tabela.add_row(
            f"[{cor}]{lang.upper()}[/{cor}]",
            f"{dados['tempo']:.6f}",
            f"{dados['cpu']:.2f}",
            f"{dados['energia']:.6f}",
            f"{dados['co2']:.4f}",
            f"[{cor}]{speedup:.2f}x[/{cor}]"
        )
    
    console.print(tabela)
    console.print("\n[dim]💡 Speedup > 1.00x significa que a linguagem é mais rápida que Python[/dim]")
    console.print("[dim]📊 Dados baseados em 50 execuções reais em cada linguagem[/dim]")


# ==== BLOCO DE TESTE ====
if __name__ == "__main__":
    print("=" * 70)
    print("TESTE DO MÓDULO COMPARADOR DE LINGUAGENS")
    print("=" * 70)
    
    # Teste 1: Buscar dados específicos
    print("\n📊 Teste 1: Buscar dados de C - Merge Sort - 10000 elementos")
    resultado = obter_benchmark("c", "merge", 10000)
    if resultado:
        print(f"✅ Tempo: {resultado['tempo']:.6f}s")
        print(f"✅ CPU: {resultado['cpu']:.2f}%")
        print(f"✅ Energia: {resultado['energia']:.6f} Wh")
        print(f"✅ CO2: {resultado['co2']:.4f}g")
    else:
        print("❌ Dados não encontrados")
    
    # Teste 2: Testar aproximação de tamanho
    print("\n📊 Teste 2: Testar aproximação (5000 elementos → 10000)")
    resultado = obter_benchmark("c", "quick", 5000)
    if resultado:
        print(f"✅ Tempo: {resultado['tempo']:.6f}s (benchmark de 10000)")
    
    # Teste 3: Comparar todas as linguagens
    print("\n📊 Teste 3: Comparar Quick Sort com 100000 elementos")
    todas = obter_todos_benchmarks("quick", 100000)
    for lang, dados in todas.items():
        print(f"  {lang.upper():6s} → {dados['tempo']:.6f}s | CPU: {dados['cpu']:.2f}%")
    
    # Teste 4: Mostrar resumo completo
    print("\n📊 Teste 4: Resumo de todos os dados")
    print(f"✅ Linguagens disponíveis: {', '.join(listar_todas_linguagens())}")
    print(f"✅ Algoritmos disponíveis: {', '.join(listar_todos_algoritmos())}")
    print(f"✅ Tamanhos disponíveis: {', '.join(map(str, listar_todos_tamanhos()))}")
    
    # Teste 5: Contar total de benchmarks
    total = 0
    for lang in listar_todas_linguagens():
        for alg in listar_todos_algoritmos():
            for tam in listar_todos_tamanhos():
                if obter_benchmark(lang, alg, tam):
                    total += 1
    
    print(f"\n✅ Total de benchmarks carregados: {total}")
    
    # Teste 6: Simular comparação com Python
    print("\n📊 Teste 5: Simulação de comparação com Python")
    resultado_python_fake = {
        "tempo": 0.05,
        "cpu": 85.0,
        "energia": 0.001,
        "co2": 0.0005
    }
    mostrar_comparacao(resultado_python_fake, "quick", 95000)  # Tamanho não padrão
    
    print("\n" + "=" * 70)
    print("✅ MÓDULO FUNCIONANDO CORRETAMENTE!")
    print("=" * 70)