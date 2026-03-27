def F1(n):
    # Caso base
    if n == 0:
        return 1
    
    # Recursão
    return F1(n - 1) + n + 1


def F2(n):
    # Caso base
    if n == 1:
        return 1
    
    # Recursão
    return F2(n - 1) + 3*n + 2


# Teste
n = int(input("Insira o valor de n: "))
print("Resultado F1(n):", F1(n))
print("Resultado F2(n):", F2(n))