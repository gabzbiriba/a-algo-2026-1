import time
import sys

sys.setrecursionlimit(2000)

def fatorial(n):
    if n == 0:
        return 1
    
    return n * fatorial(n-1)

valores = [10,100,500,1000]

for n in valores:
    print(f"\nCalculando fatorial de {n}")
    inicio = time.time()
    resultado = fatorial(n)
    fim = time.time()
    print("Tempo:", fim-inicio, "segundos")