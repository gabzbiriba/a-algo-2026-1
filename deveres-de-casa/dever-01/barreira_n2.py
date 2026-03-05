import random
import time

def insertion_sort(lista):
    for i in range(1, len(lista)):
        chave = lista[i]
        j = i - 1

        while j >= 0 and lista[j] > chave:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = chave

    return lista

def gerar_lista(n):
    lista = []
    for _ in range(n):
        lista.append(random.randint(0,100000))
    return lista

tamahos = [1000, 5000, 10000, 20000, 50000]

for n in tamahos:
    lista_original = gerar_lista(n)

    lista1 = lista_original.copy()
    lista2 = lista_original.copy()

    print(f"\nTestando com n = {n}")

    inicio = time.time()
    insertion_sort(lista1)
    fim = time.time()

    print("Insertion sort:", fim - inicio, "segundos")

    inicio = time.time()
    sorted(lista2)
    fim = time.time()

    print("Sorted (Timsort):", fim - inicio, "segundos")