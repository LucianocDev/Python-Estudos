# Compreensão de Listas (List Comprehensions) em Python

Exercicios ex019, ex020, ex021 (pasta de exercicios).

A compreensão de listas, ou *list comprehension*, é uma característica do Python que oferece uma sintaxe mais curta, elegante e muitas vezes mais eficiente para criar listas[1, 2, 5, 6, 8]. Ela permite gerar uma nova lista aplicando uma expressão a cada item de uma sequência ou iterável existente, opcionalmente filtrando itens com base em uma condição[4, 6]. Essencialmente, combina um loop `for` e, opcionalmente, uma condição `if` (ou `if-else`) em uma única linha concisa[2, 4].

## Sintaxe Básica

A estrutura fundamental de uma compreensão de lista é[1, 4, 6, 8]:

nova_lista = [expressao for item in iteravel]

text

Onde:
*   `nova_lista`: A lista resultante que será criada.
*   `expressao`: A operação ou valor a ser aplicado a cada `item` para gerar os elementos da nova lista.
*   `item`: Uma variável que representa cada elemento do `iteravel` em cada iteração.
*   `iteravel`: Uma sequência existente (como lista, tupla, string, `range`, etc.) sobre a qual iterar[5, 7].

**Exemplo 1: Criar uma lista com os quadrados dos números de 0 a 9.**

Forma tradicional com `for` loop:
quadrados = []
for numero in range(10):
quadrados.append(numero ** 2)
print(quadrados)

Output:
text

Usando compreensão de lista:
quadrados = [numero ** 2 for numero in range(10)]
print(quadrados)

Output:
text
Neste caso, `numero ** 2` é a `expressao`, `numero` é o `item` e `range(10)` é o `iteravel`[1, 3].

**Exemplo 2: Converter uma lista de palavras para maiúsculas.**
palavras = ['python', 'programação', 'list comprehension']
maiusculas = [palavra.upper() for palavra in palavras]
print(maiusculas)

Output: ['PYTHON', 'PROGRAMAÇÃO', 'LIST COMPREHENSION']
text
Aqui, a expressão é `palavra.upper()`[1, 3].

## Adicionando Condições (Filtragem)

É possível adicionar uma cláusula `if` ao final da compreensão de lista para incluir apenas os itens que satisfazem uma determinada condição[2, 3, 6].

Sintaxe:
nova_lista = [expressao for item in iteravel if condicao]

text

**Exemplo 3: Criar uma lista apenas com números pares de 0 a 10.**
numeros = range(11) # 0 a 10
pares = [num for num in numeros if num % 2 == 0]
print(pares)

Output:
text
A condição `if num % 2 == 0` filtra os elementos, incluindo apenas os pares na lista resultante[3, 6].

**Exemplo 4: Filtrar frutas que contêm a letra 'a'.**
frutas = ["apple", "banana", "cherry", "kiwi", "mango"]
frutas_com_a = [fruta for fruta in frutas if "a" in fruta]
print(frutas_com_a)

Output: ['apple', 'banana', 'mango']
text
A condição `if "a" in fruta` seleciona apenas as strings que contêm a letra 'a'[2].

## Expressões Condicionais (if-else)

Você pode usar uma estrutura `if-else` diretamente na `expressao` para aplicar lógicas diferentes com base em uma condição para cada item. Note que a ordem é diferente da cláusula `if` de filtragem.

Sintaxe:
nova_lista = [expressao_se_verdadeiro if condicao else expressao_se_falso for item in iteravel]

text

**Exemplo 5: Criar uma lista substituindo números pares por 'par' e ímpares por 'ímpar'.**
numeros = range(5) # 0 a 4
par_ou_impar = ['par' if num % 2 == 0 else 'ímpar' for num in numeros]
print(par_ou_impar)

Output: ['par', 'ímpar', 'par', 'ímpar', 'par']
text
Aqui, a expressão condicional `('par' if num % 2 == 0 else 'ímpar')` é avaliada para cada `num` no `range`[8].

**Exemplo 6: Calcular o cubo de números positivos e o quadrado de números negativos.**
numeros = range(-5, 6) # -5 a 5
resultado = [x3 if x >= 0 else x2 for x in numeros]
print(resultado)

Output:
text
A expressão `x**3 if x >= 0 else x**2` aplica a operação correta baseada no sinal de `x`[4].

## Compreensões de Lista Aninhadas

É possível usar compreensões de lista dentro de outras para criar estruturas mais complexas, como listas de listas (matrizes)[6].

**Exemplo 7: Criar uma matriz 3x3 (lista de listas).**
matriz = [[(linha * 3) + col + 1 for col in range(3)] for linha in range(3)]
print(matriz)

Output: [,,]
text
O loop externo `for linha in range(3)` define as linhas, e o loop interno `for col in range(3)` define os elementos de cada linha[6].

## Benefícios e Considerações

*   **Concisenção e Legibilidade:** Tornam o código mais curto e, para casos simples a moderados, mais fácil de ler do que loops `for` tradicionais[1, 4, 6].
*   **Performance:** Frequentemente são mais rápidas que loops `for` equivalentes para criar listas, pois as iterações ocorrem em um nível otimizado em C (na implementação CPython)[5, 7].
*   **Elegância:** São consideradas uma forma "Pythônica" e elegante de manipular listas[6].

**Cuidado:** Embora poderosas, compreensões de lista excessivamente complexas (com múltiplas condições ou aninhamentos profundos) podem se tornar difíceis de ler e entender. Nesses casos, um loop `for` tradicional pode ser preferível para manter a clareza[6].

Em resumo, a compreensão de listas é uma ferramenta poderosa e eficiente em Python para criar e manipular listas de forma concisa, sendo aplicável a uma vasta gama de tarefas, desde simples transformações e filtragens até a criação de estruturas de dados complexas[5, 6, 7, 8].