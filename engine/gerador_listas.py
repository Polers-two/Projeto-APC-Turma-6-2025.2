# engine/gerador_listas.py

import random

def gerar_listas():
    """
    Gera três listas com tamanhos diferentes:
    - 1.000 elementos
    - 10.000 elementos
    - 100.000 elementos

    Cada lista contém números inteiros aleatórios de 0 a 1.000.000.
    Retorna um dicionário com as listas.
    """
    tamanhos = [1000, 10000, 100000]
    listas = {}

    for tamanho in tamanhos:
        lista = [random.randint(0, 1_000_000) for _ in range(tamanho)]
        listas[tamanho] = lista

    return listas


def mostrar_info_listas(listas):
    """
    Exibe informações básicas sobre as listas geradas.
    """
    print("\nListas geradas com sucesso:")
    for tamanho, lista in listas.items():
        print(f"- Lista com {tamanho} elementos (exemplo: {lista[:5]} ...)")
