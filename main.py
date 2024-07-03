import gerador
import ordenadores
import time


k = int(input("Informe o valor de k (amplitude dos elementos da lista, partindo de 0): "))
n = int(input("Informe o valor de n (tamanho da lista): "))

lista = gerador.geraListaAleatoria(n, k)
print("----Lista Inicial-------")
print(f"Lista gerada: {lista}")
print("------------------")
print()

print(f"----Bubble-------")
inicio = time.time()
print(f"Lista ordenada: {ordenadores.bubbleSort(n, lista)}")
fim = time.time()
print(f"Tempo de exec em ms: { (fim - inicio) * 1000 }")
print()

print(f"----Selection-------")
inicio = time.time()
print(f"Lista ordenada: {ordenadores.selectionSort(n, lista)}")
fim = time.time()
print(f"Tempo de exec em ms: { (fim - inicio) * 1000 }")
print()

print(f"----Insertion-------")
inicio = time.time()
print(f"Lista ordenada: {ordenadores.insertionSort(n, lista)}")
fim = time.time()
print(f"Tempo de exec em ms: { (fim - inicio) * 1000 }")
print()

print(f"----Merge-------")
inicio = time.time()
print(f"Lista ordenada: {ordenadores.mergeSort(lista)}")
fim = time.time()
print(f"Tempo de exec em ms: { (fim - inicio) * 1000 }")
print()

print(f"----Counting-------")
inicio = time.time()
print(f"Lista ordenada: { ordenadores.countingSort(n, k, lista)}")
fim = time.time()
print(f"Tempo de exec em ms: { (fim - inicio) * 1000 }")
print()