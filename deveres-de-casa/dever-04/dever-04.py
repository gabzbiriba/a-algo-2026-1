def F(n):
    # Caso base
    if n == 1:
        return 2
    
    # Recursão
    return 2 * F(n-1) + n**2

# Teste
n = int(input("Insira o valor de n: "))
print("Resultado:", F(n))