from random import randint

def geraListaAleatoria (tamanho:int, valorMaximo:int) -> list:
    lista = []
    for i in range(tamanho): lista.append(randint(0,valorMaximo))
    return lista