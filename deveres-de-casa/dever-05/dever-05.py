import math

def teorema_mestre(a, b, k, p=0, label=""):
    log_b_a = math.log(a, b)
    print(f"\n{'='*50}")
    print(f"  {label}")
    print(f"  a={a}, b={b}, f(n)=n^{k} · log^{p}(n)")
    print(f"  log_{b}({a}) = {log_b_a:.4f}")

    if k < log_b_a:
        print(f"  → Caso 1: T(n) = Θ(n^{log_b_a:.4f})")
    elif k == log_b_a:
        print(f"  → Caso 2: T(n) = Θ(n^{k} · log(n))")
    else:
        print(f"  → Caso 3: T(n) = Θ(n^{k})")

teorema_mestre(a=2,  b=4, k=0.5, label="T(n) = 2T(n/4) + √n")
teorema_mestre(a=2,  b=4, k=1,   label="T(n) = 2T(n/4) + n")
teorema_mestre(a=16, b=4, k=2,   label="T(n) = 16T(n/4) + n²")

teorema_mestre(a=2, b=2, k=1, label="Merge Sort: T(n) = 2T(n/2) + n")
teorema_mestre(a=8, b=2, k=2, label="Multiplicação de Matrizes: T(n) = 8T(n/2) + n²")