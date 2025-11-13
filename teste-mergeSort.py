# teste com merge sort

# Energia estimada (kWh):
# E = (P_CPU × T) / 3600
# onde:
# P_CPU = potência média da CPU (em watts)
# T = tempo de execução (em segundos)

import random
import psutil
import time

inicio = time.time()
def mergeSort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  leftHalf = arr[:mid]
  rightHalf = arr[mid:]

  sortedLeft = mergeSort(leftHalf)
  sortedRight = mergeSort(rightHalf)

  return merge(sortedLeft, sortedRight)

def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

mylist = []
for i in range(10000):
  mylist.append(random.uniform(1, 1000))

mysortedlist = mergeSort(mylist)
print("Sorted array:", mysortedlist)

fim = time.time()
tempo = fim - inicio
uso_medio_cpu = psutil.cpu_percent(interval=None)

consumo_estimado = (uso_medio_cpu / 100) * 65 # 65W
energia_estimada = (consumo_estimado * tempo) / 3600

print(f"segundos para execução: {tempo:.2f}")
print(f"Uso médio da CPU: {uso_medio_cpu}%")
print(f"Energia estimada gasta kWh: {energia_estimada:.15f}")