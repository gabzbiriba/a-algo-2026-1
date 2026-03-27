def potencia_de_2(n):
    return n > 0 and (n & (n - 1)) == 0

def F3(n):
    # Caso base
    if n == 1:
        return 5
    
    # Recursão
    return F3(n//2) + 3

# Teste
n = int(input("Insira um valor de n (potência de 2): "))
if not potencia_de_2(n):
    print("O número precisa ser potência de 2!")
else:
    print("Resultado F3(n):", F3(n))