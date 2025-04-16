# Operadores Lógicos em Python

Em Python, os operadores lógicos são utilizados para combinar ou modificar valores booleanos (`True` ou `False`). Eles são fundamentais para construir condições complexas em instruções de controle de fluxo (como `if`, `elif`, `else`, `while`) e para realizar operações lógicas em geral.

## Operadores Lógicos Disponíveis

Python oferece três operadores lógicos principais:

- `and` (E lógico)
- `or` (OU lógico)
- `not` (NÃO lógico)

---

## 1. Operador `and`

O operador `and` retorna `True` se **ambos** os operandos forem verdadeiros. Caso contrário, ele retorna `False`.

### Tabela Verdade do `and`

| Operando 1 | Operando 2 | Resultado (`Operando 1 and Operando 2`) |
|------------|------------|-----------------------------------------|
| True       | True       | True                                    |
| True       | False      | False                                   |
| False      | True       | False                                   |
| False      | False      | False                                   |

### Exemplos

```python
x = 5
y = 10

resultado1 = (x > 0) and (y < 15)
print(f"(x > 0) and (y < 15): {resultado1}")  # True

resultado2 = (x < 0) and (y < 15)
print(f"(x < 0) and (y < 15): {resultado2}")  # False

resultado3 = (x < 0) and (y > 15)
print(f"(x < 0) and (y > 15): {resultado3}")  # False
```

### Curto-Circuito do `and`

```python
def funcao_verdadeira():
    print("Função verdadeira foi chamada.")
    return True

def funcao_falsa():
    print("Função falsa foi chamada.")
    return False

resultado4 = funcao_falsa() and funcao_verdadeira()
print(f"funcao_falsa() and funcao_verdadeira(): {resultado4}")  # False

resultado5 = funcao_verdadeira() and funcao_verdadeira()
print(f"funcao_verdadeira() and funcao_verdadeira(): {resultado5}") # True
```

---

## 2. Operador `or`

O operador `or` retorna `True` se **pelo menos um** dos operandos for verdadeiro. Ele retorna `False` apenas se **ambos** forem falsos.

### Tabela Verdade do `or`

| Operando 1 | Operando 2 | Resultado (`Operando 1 or Operando 2`) |
|------------|------------|----------------------------------------|
| True       | True       | True                                   |
| True       | False      | True                                   |
| False      | True       | True                                   |
| False      | False      | False                                  |

### Exemplos

```python
idade = 25
tem_carteira = False

pode_dirigir = (idade >= 18) or tem_carteira
print(f"(idade >= 18) or tem_carteira: {pode_dirigir}")  # True

tem_passaporte = True
tem_visto = False
pode_viajar = tem_passaporte or tem_visto
print(f"tem_passaporte or tem_visto: {pode_viajar}")  # True

esta_chovendo = False
tem_guarda_chuva = False
precisa_correr = esta_chovendo or not tem_guarda_chuva
print(f"esta_chovendo or not tem_guarda_chuva: {precisa_correr}")  # True
```

### Curto-Circuito do `or`

```python
def funcao_verdadeira():
    print("Função verdadeira foi chamada.")
    return True

def funcao_falsa():
    print("Função falsa foi chamada.")
    return False

resultado6 = funcao_verdadeira() or funcao_falsa()
print(f"funcao_verdadeira() or funcao_falsa(): {resultado6}")  # True

resultado7 = funcao_falsa() or funcao_verdadeira()
print(f"funcao_falsa() or funcao_verdadeira(): {resultado7}")  # True
```

---

## 3. Operador `not`

O operador `not` inverte o valor booleano do operando.

### Tabela Verdade do `not`

| Operando | Resultado (`not Operando`) |
|----------|-----------------------------|
| True     | False                       |
| False    | True                        |

### Exemplos

```python
esta_logado = False
nao_esta_logado = not esta_logado
print(f"not esta_logado: {nao_esta_logado}")  # True

numero_positivo = 10
nao_eh_positivo = not (numero_positivo > 0)
print(f"not (numero_positivo > 0): {nao_eh_positivo}")  # False

tem_permissao = True
sem_permissao = not tem_permissao
print(f"not tem_permissao: {sem_permissao}")  # False
```

---

## Precedência dos Operadores Lógicos

Ordem de precedência em Python:

1. `not`
2. `and`
3. `or`

Use parênteses para alterar a ordem de avaliação.

### Exemplos

```python
a = True
b = False
c = True

resultado8 = not a and b or c
print(f"not a and b or c: {resultado8}")  # True

resultado9 = not (a and b) or c
print(f"not (a and b) or c: {resultado9}")  # True

resultado10 = not (a and (b or c))
print(f"not (a and (b or c)): {resultado10}")  # False
```

---

## Operadores Lógicos em Controle de Fluxo

```python
temperatura = 25
esta_chovendo = False

if temperatura > 20 and not esta_chovendo:
    print("O clima está agradável.")

idade = 16
tem_autorizacao = True

if idade >= 18 or tem_autorizacao:
    print("Pode entrar.")
else:
    print("Acesso negado.")

contador = 0
while contador < 10 and not (contador % 2 != 0):
    print(contador)
    contador += 1
```

---

## Truthy e Falsy em Python

### Valores Falsy:

- `False`
- `None`
- `0`, `0.0`, `0j`
- `""`, `[]`, `()`, `{}`, `set()`, `dict()`

Todos os outros valores são considerados **Truthy**.

### Comportamento dos Operadores:

- `and`: retorna o primeiro valor falso ou o último valor verdadeiro.
- `or`: retorna o primeiro valor verdadeiro ou o último valor falso.
- `not`: retorna sempre `True` ou `False`.

### Exemplos

```python
nome = "João"
idade = 0
lista = [1, 2, 3]
vazia = []

print(f"nome and idade: {nome and idade}")  # 0
print(f"idade and nome: {idade and nome}")  # 0
print(f"lista and nome: {lista and nome}")  # João
print(f"vazia or nome: {vazia or nome}")    # João
print(f"nome or vazia: {nome or vazia}")    # João
print(f"not nome: {not nome}")              # False
print(f"not idade: {not idade}")            # True
```

---

## Conclusão

Os operadores lógicos (`and`, `or`, `not`) são essenciais em Python para construir condições, controlar o fluxo de execução e lidar com valores booleanos e não booleanos. Entender suas regras de precedência, comportamento de curto-circuito e interação com valores truthy e falsy é fundamental para escrever códigos claros e eficientes.