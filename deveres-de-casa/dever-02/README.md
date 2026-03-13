# Explicação sobre o Dever 02

**Análise de complexidade** 

O algoritmo do fatorial recursivo chama a si mesmo uma vez para cada valor de n, ou seja, o número de chamadas cresce linearmente com n.

Exemplo:
 *fatorial(n)*
 *fatorial(n-1)*
 *fatorial(n-2)*
 *...*
 *fatorial(0)*

A relação de recorrência é:

*T(n) = T(n-1) + 1*

Resolvendo a recorrência:

*T(n) = n*

Logo, a complexidade assintótica do algoritmo é:

*O(n)*

Isso significa que o tempo de execução é **diretamente proporcional** ao tamanho da entrada.

No código foi utilizado *sys* e *setrecursionlimit* para evitar que o Pyhton limite a recursão do tamanho n = 1000, evitando assim o erro de *maximum recursion depth exceeded*.