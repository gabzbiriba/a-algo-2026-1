import math

def analisar_teorema_mestre(a, b, k, p):
    """
    T(n) = a*T(n/b) + n^k * log^p(n)
    Compara f(n) = n^k com n^(log_b(a))
    """
    log_b_a = math.log(a, b)
    print(f"\nEntrada: a={a}, b={b}, k={k}, p={p}, f(n) = n^{k} * log^{p}(n)")
    print(f"log_{b}({a}) = {log_b_a:.4f}")

    if k < log_b_a:
        print("Caso do Teorema Mestre: Caso 1")
        print(f"Resultado: T(n) = Θ(n^{log_b_a:.4f})")

    elif k == log_b_a:
        print("Caso do Teorema Mestre: Caso 2")
        if p > -1:
            print(f"Resultado: T(n) = Θ(n^{k} * log^{p+1}(n))")
        elif p == -1:
            print(f"Resultado: T(n) = Θ(n^{k} * log(log(n)))")
        else:
            print(f"Resultado: T(n) = Θ(n^{k})")

    else:
        print("Caso do Teorema Mestre: Caso 3")
        print(f"Resultado: T(n) = Θ(n^{k} * log^{p}(n))")


a = int(input("Digite o valor de a (nº de subproblemas): "))
b = int(input("Digite o valor de b (fator de redução): "))
k = int(input("Digite o valor de k (expoente de n em f(n)): "))
p = int(input("Digite o valor de p (expoente de log(n) em f(n)): "))

analisar_teorema_mestre(a, b, k, p)