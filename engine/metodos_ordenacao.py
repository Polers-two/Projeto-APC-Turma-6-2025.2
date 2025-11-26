"""
Módulo com implementações de algoritmos de ordenação
Todos os algoritmos retornam uma nova lista ordenada sem modificar a original
"""
import random


def bubble_sort(lista):
    """
    Algoritmo Bubble Sort - O(n²)
    Compara elementos adjacentes e os troca se estiverem na ordem errada
    
    Args:
        lista: Lista de elementos comparáveis
    
    Returns:
        Nova lista ordenada
    """
    lista = lista[:]
    n = len(lista)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
    return lista


def insertion_sort(lista):
    """
    Algoritmo Insertion Sort - O(n²)
    Constrói a lista ordenada um elemento por vez
    
    Args:
        lista: Lista de elementos comparáveis
    
    Returns:
        Nova lista ordenada
    """
    lista = lista[:]
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1
        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = chave
    return lista


def merge_sort(lista):
    """
    Algoritmo Merge Sort - O(n log n)
    Divide a lista recursivamente e depois mescla as partes ordenadas
    
    Args:
        lista: Lista de elementos comparáveis
    
    Returns:
        Nova lista ordenada
    """
    if len(lista) <= 1:
        return lista[:]
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])
    direita = merge_sort(lista[meio:])
    return merge(esquerda, direita)


def merge(esquerda, direita):
    """
    Função auxiliar do Merge Sort que mescla duas listas ordenadas
    
    Args:
        esquerda: Lista ordenada
        direita: Lista ordenada
    
    Returns:
        Lista mesclada e ordenada
    """
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    return resultado + esquerda[i:] + direita[j:]


def quick_sort(lista):
    """
    Algoritmo Quick Sort - O(n log n) médio, O(n²) pior caso
    Escolhe um pivô e particiona a lista em elementos menores e maiores
    
    Args:
        lista: Lista de elementos comparáveis
    
    Returns:
        Nova lista ordenada
    """
    if len(lista) <= 1:
        return lista[:]
    pivo = lista[0]
    menores = [x for x in lista[1:] if x <= pivo]
    maiores = [x for x in lista[1:] if x > pivo]
    return quick_sort(menores) + [pivo] + quick_sort(maiores)


def esta_ordenada(lista):
    """
    Verifica se uma lista está ordenada
    
    Args:
        lista: Lista a ser verificada
    
    Returns:
        True se ordenada, False caso contrário
    """
    return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))


def bogosort(lista):
    """
    Algoritmo Bogosort - O((n+1)!) - APENAS PARA FINS EDUCACIONAIS
    Embaralha a lista aleatoriamente até que esteja ordenada
    ATENÇÃO: Extremamente ineficiente! Use apenas com listas pequenas (≤10 elementos)
    
    Args:
        lista: Lista de elementos comparáveis (máximo 10 elementos)
    
    Returns:
        Nova lista ordenada
    """
    lista = lista[:]
    while not esta_ordenada(lista):
        random.shuffle(lista)
    return lista