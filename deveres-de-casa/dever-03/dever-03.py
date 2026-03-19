def palindromo(arr):

    # Caso base: se o tamanho for igual à 0 ou 1, é um palíndromo 
    if len(arr) <=1:
        return True
    
    # Compara o primeiro com o último
    if arr[0] != arr[-1]:
        return False
    
    # Resolve subproblema menor
    return palindromo(arr[1:-1])

# Exemplos

array1 = [0, 1, 2, 3, 2, 1, 0]
array2 = ["a", "b", "b", "a"]
array3 = ["a", "b", "c", "b", "a"]
array4 = ["a", "b", "c", "f", "b", "a"]

print(palindromo(array1))
print(palindromo(array2))
print(palindromo(array3))
print(palindromo(array4))