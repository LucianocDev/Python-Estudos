
# Aula PYCODEBR — Manipulação de Strings em Python

## Índices dos caracteres

```
A U L A   P  A  Y  C  O  D  E  B  R
0 1 2 3 4 5  6  7  8  9  10 11 12 13
```

A variável `texto = 'AULA PAYCODEBR'` é tratada como uma cadeia de caracteres (string), partindo do índice `[0]`.  
Usando a variável `texto[]` podemos solicitar a apresentação de um ou mais caracteres.

---

## Exemplo 01

```python
texto = 'AULA PAYCODEBR'
texto[0]
```

**Saída:**

```
'A'
```

Nesse exemplo, solicitamos o caractere na posição `[0]`, que é a letra `'A'`.

---

## Exemplo 02

```python
texto = 'AULA PAYCODEBR'
texto[5:11]
```

**Saída:**

```
'PYCODE'
```

Nesse exemplo, pedimos do caractere no índice 5 até o 11 (lembrando que o caractere de índice final **não é incluído** na exibição, ou seja, vai do 5 até o 10).

---

## Exemplo 03

```python
texto = 'AULA PAYCODEBR'
texto[5:]
```

**Saída:**

```
'PYCODEBR'
```

Ao omitir o índice final, o Python exibe todos os caracteres a partir do índice 5 até o final da string.

Também é possível fazer o contrário:

```python
texto[:5]
```

**Saída:**

```
'AULA '
```

---

## Função `len()`

Exibe a quantidade de caracteres da string.

### Exemplo 04

```python
texto = 'AULA PAYCODEBR'
len(texto)
```

**Saída:**

```
13
```

---

## Função `count()`

Conta quantas vezes um caractere ou sequência aparece na string.

### Exemplo 05

```python
texto = 'AULA PAYCODEBR'
texto.count('A')        # Saída: 2
texto.count('AULA')     # Saída: 1
texto.count('A', 5, 11) # Saída: 0
```

---

## Função `find()`

Retorna o índice de onde a sequência de caracteres começa.

### Exemplo 06

```python
texto = 'AULA PAYCODEBR'
texto.find('AULA')      # Saída: 0
texto.find('PYCODEBR')  # Saída: 5
```

---

## Função `upper()`

Coloca todos os caracteres em **maiúsculas**.

### Exemplo 07

```python
texto = 'AULA PAYCODEBR'
texto.upper()
```

**Saída:**

```
'AULA PAYCODEBR'
```

---

## Função `lower()`

Coloca todos os caracteres em **minúsculas**.

### Exemplo 08

```python
texto = 'AULA PAYCODEBR'
texto.lower()
```

**Saída:**

```
'aula paycodebr'
```

---

## Função `capitalize()`

Coloca a **primeira letra** da string em maiúscula.

### Exemplo 09

```python
texto = 'aula pycodebr'
texto.capitalize()
```

**Saída:**

```
'Aula pycodebr'
```

---

## Função `title()`

Coloca a **primeira letra de cada palavra** da string em maiúscula.

### Exemplo 10

```python
texto = 'aula pycodebr'
texto.title()
```

**Saída:**

```
'Aula Pycodebr'
```

---

## Função `split()`

Divide a string em uma lista, separando pelas palavras.

### Exemplo 11

```python
texto = 'AULA PAYCODEBR'
texto.split()
```

**Saída:**

```python
['AULA', 'PYCODEBR']
```

---

## Função `join()`

Utilizada para unir elementos de uma lista em uma única string, usando um separador.

### Exemplo 12

```python
texto = 'AULA PAYCODEBR'
lista_de_palavras = texto.split()
'_'.join(lista_de_palavras)
```

**Saída:**

```
'AULA_PAYCODEBR'
```
