def bubbleSort(tamanho:int, lista:list) -> list:
  listaCopia = lista[::]
  for i in range(tamanho):
      for j in range(0, tamanho-i-1):
          if listaCopia[j] > listaCopia[j+1]:
              listaCopia[j], listaCopia[j+1] = listaCopia[j+1], listaCopia[j]
  return listaCopia


def selectionSort(tamanho:int, lista:list) -> list:
  listaCopia = lista[::]
  for i in range(tamanho):
      min_index = i
      for j in range(i+1, tamanho):
          if listaCopia[min_index] > listaCopia[j]:
              min_index = j
      listaCopia[i], listaCopia[min_index] = listaCopia[min_index], listaCopia[i]
  return listaCopia

def insertionSort(tamanho:int, lista:list) -> list:
  listaCopia = lista[::]
  for i in range(1, tamanho):
      chave = listaCopia[i]
      j = i-1
      while j >= 0 and chave < listaCopia[j]:
          listaCopia[j+1] = listaCopia[j]
          j -= 1
      listaCopia[j+1] = chave
  return listaCopia

def countingSort(tamanho:int, amplitude:int, lista:list) -> list:
  listaCopia = lista[::]
  maximo = amplitude
  minimo = 0
  range_ = maximo - minimo + 1
  count = [0]*range_
  saida = [0]*tamanho
  for i in range(tamanho):
    count[listaCopia[i]-minimo] += 1
  for i in range(1, len(count)):
    count[i] += count[i-1]
  for i in range(tamanho-1, -1, -1):
    saida[count[listaCopia[i]-minimo]-1] = listaCopia[i]
    count[listaCopia[i]-minimo] -= 1
  for i in range(tamanho):
    listaCopia[i] = saida[i]
  return listaCopia

def mergeSort(lista):
  if len(lista) > 1:
      meio = len(lista) // 2
      esquerda = mergeSort(lista[:meio])
      direita = mergeSort(lista[meio:])

      listaCopia = []
      i = j = 0
      while i < len(esquerda) and j < len(direita):
          if esquerda[i] < direita[j]:
              listaCopia.append(esquerda[i])
              i += 1
          else:
              listaCopia.append(direita[j])
              j += 1

      while i < len(esquerda):
          listaCopia.append(esquerda[i])
          i += 1

      while j < len(direita):
          listaCopia.append(direita[j])
          j += 1

      return listaCopia
  else:
      return lista