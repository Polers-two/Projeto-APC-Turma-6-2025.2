"""
Modulo de algoritmos de ordenacao
Implementa varios metodos para ordenar listas de numeros
"""
import random


def bubble_sort(lista):
    """
    Bubble Sort - Compara elementos adjacentes e troca se necessario
    Complexidade: O(n²)
    """
    lista_copia = lista[:]
    tamanho = len(lista_copia)
    
    for i in range(tamanho - 1):
        for j in range(tamanho - i - 1):
            if lista_copia[j] > lista_copia[j + 1]:
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
    
    return lista_copia


def insertion_sort(lista):
    """
    Insertion Sort - Insere cada elemento na posicao correta
    Complexidade: O(n²)
    """
    lista_copia = lista[:]
    
    for i in range(1, len(lista_copia)):
        elemento_atual = lista_copia[i]
        posicao = i - 1
        
        while posicao >= 0 and lista_copia[posicao] > elemento_atual:
            lista_copia[posicao + 1] = lista_copia[posicao]
            posicao = posicao - 1
        
        lista_copia[posicao + 1] = elemento_atual
    
    return lista_copia


def merge_sort(lista):
    """
    Merge Sort - Divide a lista em partes menores e depois junta ordenando
    Complexidade: O(n log n)
    """
    if len(lista) <= 1:
        return lista[:]
    
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    
    return juntar_listas(esquerda, direita)


def juntar_listas(esquerda, direita):
    """
    Funcao auxiliar do Merge Sort
    Junta duas listas ordenadas em uma lista ordenada
    """
    resultado = []
    i = 0
    j = 0
    
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i = i + 1
        else:
            resultado.append(direita[j])
            j = j + 1
    
    while i < len(esquerda):
        resultado.append(esquerda[i])
        i = i + 1
    
    while j < len(direita):
        resultado.append(direita[j])
        j = j + 1
    
    return resultado


def quick_sort(lista):
    """
    Quick Sort - Escolhe um pivo e separa elementos menores e maiores
    Complexidade: O(n log n) em media
    """
    if len(lista) <= 1:
        return lista[:]
    
    pivo = lista[0]
    menores = []
    maiores = []
    
    for i in range(1, len(lista)):
        if lista[i] <= pivo:
            menores.append(lista[i])
        else:
            maiores.append(lista[i])
    
    return quick_sort(menores) + [pivo] + quick_sort(maiores)


def verificar_ordenada(lista):
    """
    Verifica se uma lista esta em ordem crescente
    """
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True


def bogosort(lista):
    """
    Bogosort - Embaralha ate ficar ordenado
    Complexidade: O((n+1)!) 
    Use apenas com listas pequenas (ate 10 elementos)
    """
    lista_copia = lista[:]
    
    while not verificar_ordenada(lista_copia):
        random.shuffle(lista_copia)
    
    return lista_copia
