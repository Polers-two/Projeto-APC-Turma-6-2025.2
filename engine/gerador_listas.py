"""
Modulo para gerar listas de teste
Cria listas aleatorias de diferentes tamanhos
"""
import random
from rich.table import Table
from rich import print


def gerar_listas(tamanhos=None):
    """
    Gera listas aleatorias para testes
    
    Parametros:
        tamanhos: Lista com tamanhos desejados
    
    Retorna:
        Dicionario onde a chave e o tamanho e o valor e a lista
    """
    if tamanhos is None:
        tamanhos = [10, 1000, 10000, 100000]
    
    listas = {}
    
    for tamanho in tamanhos:
        lista = []
        for i in range(tamanho):
            numero = random.randint(0, 1000000)
            lista.append(numero)
        listas[tamanho] = lista
    
    return listas


def mostrar_info_listas(listas):
    """
    Mostra informacoes sobre as listas geradas
    """
    tabela = Table(title="Listas geradas")
    tabela.add_column("Tamanho")
    tabela.add_column("Exemplo (primeiros elementos)")
    
    for tamanho, lista in listas.items():
        elementos_mostrar = []
        for i in range(min(6, len(lista))):
            elementos_mostrar.append(str(lista[i]))
        
        exemplo = ", ".join(elementos_mostrar)
        if len(lista) > 6:
            exemplo = exemplo + " ..."
        
        tabela.add_row(str(tamanho), exemplo)
    
    print(tabela)
