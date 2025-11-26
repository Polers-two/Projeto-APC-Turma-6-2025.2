import random
from rich.table import Table
from rich import print


def gerar_listas(tamanhos=None):
    """
    Gera listas aleatórias de diferentes tamanhos para testes
    
    Args:
        tamanhos: Lista de tamanhos desejados (padrão: [10, 1000, 10000, 100000])
    
    Returns:
        Dicionário com tamanho como chave e lista como valor
    """
    if tamanhos is None:
        tamanhos = [10, 1000, 10000, 100000]
    return {t: [random.randint(0, 1_000_000) for _ in range(t)] for t in tamanhos}


def mostrar_info_listas(listas):
    """
    Exibe informações sobre as listas geradas
    
    Args:
        listas: Dicionário com listas geradas
    """
    tabela = Table(title="Listas geradas")
    tabela.add_column("Tamanho")
    tabela.add_column("Exemplo")
    for t, lista in listas.items():
        exemplo = ", ".join(str(x) for x in lista[:6])
        tabela.add_row(str(t), exemplo + (" ..." if len(lista) > 6 else ""))
    print(tabela)