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

def countingSort(tamanho:int, amplitude:int, lista:list) -> list:
    listaFinal = [0]*tamanho
    contador = [0]*(amplitude+1)
    for i in range(tamanho): contador[lista[i]] += 1 #contagem de elementos
    for i in range(1, amplitude + 1): contador[i] += contador[i-1] #soma de prefixos
    for i in range(amplitude, 0, -1): contador[i] = contador[i-1] #shift para a direita
    contador[0] = 0
    for i in range(tamanho): #posicionamento dos elementos
        listaFinal[contador[lista[i]]] = lista[i]
        contador[lista[i]] += 1
    return listaFinal