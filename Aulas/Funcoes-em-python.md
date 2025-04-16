# Estudo Detalhado sobre Funções em Python

Funções são um dos pilares da programação em Python (e em muitas outras linguagens). Elas nos permitem organizar o código, torná-lo reutilizável e mais legível. Vamos detalhar o conceito.

## O que são Funções em Python?

Uma função é um **bloco de código nomeado** que realiza uma tarefa específica. Pense nela como uma "mini-rotina" ou um "procedimento" que você pode definir uma vez e chamar (executar) quantas vezes precisar, possivelmente com diferentes entradas.

## Por que usar Funções?

1.  **Reutilização de Código (DRY - Don't Repeat Yourself):** Se você tem um trecho de código que precisa ser executado em vários lugares, coloque-o em uma função e chame a função. Isso evita duplicação e facilita a manutenção.
2.  **Modularidade:** Quebra um programa complexo em partes menores e gerenciáveis.
3.  **Legibilidade:** Funções com nomes bem escolhidos tornam o código mais fácil de entender.
4.  **Abstração:** Permitem usar um código sem precisar saber *todos* os detalhes de como ele funciona internamente.

## Sintaxe Básica: Definindo e Chamando Funções

* **Definição:** Usa a palavra-chave `def`, seguida pelo nome da função, parênteses `()` e dois pontos `:`. O bloco de código indentado abaixo pertence à função.
* **Chamada:** Usa o nome da função seguido por parênteses `()`.

```python
# 1. Definição da função
def saudacao():
  """Esta função simples imprime uma saudação.""" # Isso é uma Docstring
  nome = "Mundo"
  print(f"Olá, {nome}!")

# 2. Chamada (execução) da função
print("Antes da função...")
saudacao()
print("Depois da função.")

# Saída:
# Antes da função...
# Olá, Mundo!
# Depois da função.
Parâmetros e Argumentos
Parâmetros: Variáveis listadas na definição da função (def func(param1, param2):).
Argumentos: Valores reais passados na chamada da função (func(arg1, arg2)).
Python

# 'nome_pessoa' é um PARÂMETRO
def saudacao_personalizada(nome_pessoa):
  """Imprime uma saudação para um nome específico."""
  print(f"Olá, {nome_pessoa}!")

# "Ana" e "Carlos" são ARGUMENTOS passados na chamada
saudacao_personalizada("Ana")
saudacao_personalizada("Carlos")

# Saída:
# Olá, Ana!
# Olá, Carlos!
Tipos de Argumentos
1. Argumentos Posicionais
São passados na ordem em que os parâmetros foram definidos. A ordem importa!

Python

def descrever_pet(tipo_animal, nome_pet):
  """Descreve um animal de estimação."""
  print(f"Eu tenho um {tipo_animal}.")
  print(f"O nome dele(a) é {nome_pet}.")

# A ordem importa: "cachorro" vai para tipo_animal, "Rex" para nome_pet
descrever_pet("cachorro", "Rex")
print("-" * 10)
# Ordem trocada = resultado diferente (e talvez errado)
descrever_pet("Fido", "gato") # Logicamente estranho

# Saída:
# Eu tenho um cachorro.
# O nome dele(a) é Rex.
# ----------
# Eu tenho um Fido.
# O nome dele(a) é gato.
2. Argumentos de Palavra-Chave (Keyword Arguments)
São passados usando nome_parametro=valor. A ordem não importa.

Python

def descrever_pet(tipo_animal, nome_pet):
  """Descreve um animal de estimação."""
  print(f"Eu tenho um {tipo_animal}.")
  print(f"O nome dele(a) é {nome_pet}.")

# Usando argumentos de palavra-chave, a ordem não importa
descrever_pet(nome_pet="Totó", tipo_animal="cachorro")
print("-" * 10)
descrever_pet(tipo_animal="gato", nome_pet="Mimi")

# Saída:
# Eu tenho um cachorro.
# O nome dele(a) é Totó.
# ----------
# Eu tenho um gato.
# O nome dele(a) é Mimi.
Nota: Argumentos posicionais devem vir antes dos de palavra-chave.

3. Valores Padrão para Parâmetros
Permite definir um valor padrão se o argumento não for passado. Parâmetros com padrão devem vir depois dos sem padrão.

Python

def potencia(base, expoente=2): # expoente tem valor padrão 2
  """Calcula a potência de um número (padrão é ao quadrado)."""
  resultado = base ** expoente
  print(f"{base} elevado a {expoente} é {resultado}")

potencia(5)      # Usa o expoente padrão (2)
potencia(3, 3)   # Passa um valor explícito para expoente (3)
potencia(base=4) # Usa o expoente padrão (2)
potencia(base=2, expoente=5) # Passa ambos explicitamente

# Saída:
# 5 elevado a 2 é 25
# 3 elevado a 3 é 27
# 4 elevado a 2 é 16
# 2 elevado a 5 é 32
4. Argumentos de Comprimento Variável (*args e **kwargs)
*args: Permite receber múltiplos argumentos posicionais extras em uma tupla. Deve vir depois dos parâmetros posicionais normais.

Python

def somar_todos(*numeros):
  """Soma todos os números passados como argumento."""
  print(f"Recebi os números: {numeros}") # numeros é uma tupla
  soma = 0
  for num in numeros:
    soma += num
  return soma # Veremos 'return' a seguir

resultado1 = somar_todos(1, 2, 3)
print(f"Soma 1: {resultado1}")
resultado2 = somar_todos(10, 20, 30, 40, 50)
print(f"Soma 2: {resultado2}")
resultado3 = somar_todos()
print(f"Soma 3: {resultado3}")

# Saída:
# Recebi os números: (1, 2, 3)
# Soma 1: 6
# Recebi os números: (10, 20, 30, 40, 50)
# Soma 2: 150
# Recebi os números: ()
# Soma 3: 0
**kwargs: Permite receber múltiplos argumentos de palavra-chave extras em um dicionário. Deve vir depois de todos os outros parâmetros.

Python

def exibir_info_usuario(id_usuario, **info_extra):
  """Exibe informações do usuário, incluindo dados extras."""
  print(f"ID do Usuário: {id_usuario}")
  print(f"Informações Extras Recebidas: {info_extra}") # info_extra é um dicionário
  for chave, valor in info_extra.items():
    print(f"- {chave.replace('_', ' ').title()}: {valor}")

exibir_info_usuario(101, nome="Alice", email="alice@exemplo.com", cidade="São Paulo")
print("-" * 20)
exibir_info_usuario(202, nome="Beto", profissao="Engenheiro")

# Saída:
# ID do Usuário: 101
# Informações Extras Recebidas: {'nome': 'Alice', 'email': 'alice@exemplo.com', 'cidade': 'São Paulo'}
# - Nome: Alice
# - Email: alice@exemplo.com
# - Cidade: São Paulo
# --------------------
# ID do Usuário: 202
# Informações Extras Recebidas: {'nome': 'Beto', 'profissao': 'Engenheiro'}
# - Nome: Beto
# - Profissao: Engenheiro
Ordem geral dos parâmetros: posicionais obrigatórios, posicionais com padrão, *args, keyword-only obrigatórios, keyword-only com padrão, **kwargs.

Valores de Retorno (return)
Funções retornam um valor usando return.

Termina a função imediatamente.
Pode ter múltiplos return (mas só um executa).
Se não houver return explícito, retorna None.
Python

def calcular_area_retangulo(largura, altura):
  """Calcula e retorna a área de um retângulo."""
  if largura < 0 or altura < 0:
    print("Erro: Largura e altura devem ser positivas.")
    return None # Retorna None explicitamente em caso de erro
  area = largura * altura
  return area # Retorna o valor calculado

# Capturando o valor retornado
area1 = calcular_area_retangulo(10, 5)
if area1 is not None:
  print(f"A área do retângulo 1 é: {area1}")

area2 = calcular_area_retangulo(-5, 10) # Causa o retorno de None
if area2 is None:
    print("Não foi possível calcular a área 2.")

# Função sem retorno explícito
def apenas_imprime(mensagem):
    print(mensagem)

resultado_impressao = apenas_imprime("Teste")
print(f"Valor retornado por apenas_imprime: {resultado_impressao}")

# Saída:
# A área do retângulo 1 é: 50
# Erro: Largura e altura devem ser positivas.
# Não foi possível calcular a área 2.
# Teste
# Valor retornado por apenas_imprime: None
Retornando Múltiplos Valores
Separados por vírgula, Python os empacota em uma tupla.

Python

import math

def calcular_circulo(raio):
  """Calcula e retorna a área e a circunferência de um círculo."""
  if raio < 0:
    return None, None # Retorna uma tupla de Nones
  area = math.pi * (raio ** 2)
  circunferencia = 2 * math.pi * raio
  return area, circunferencia # Retorna uma tupla (area, circunferencia)

# Desempacotando o retorno
a, c = calcular_circulo(10)
if a is not None:
  print(f"Raio 10 -> Área: {a:.2f}, Circunferência: {c:.2f}")

# Recebendo a tupla diretamente
resultado_tupla = calcular_circulo(5)
if resultado_tupla[0] is not None:
  print(f"Raio 5 -> Resultado (Tupla): {resultado_tupla}")
  print(f"          Área: {resultado_tupla[0]:.2f}")
  print(f"          Circunferência: {resultado_tupla[1]:.2f}")

a_err, c_err = calcular_circulo(-2)
print(f"Raio -2 -> Área: {a_err}, Circunferência: {c_err}")

# Saída:
# Raio 10 -> Área: 314.16, Circunferência: 62.83
# Raio 5 -> Resultado (Tupla): (78.53981633974483, 31.41592653589793)
#           Área: 78.54
#           Circunferência: 31.42
# Raio -2 -> Área: None, Circunferência: None
Escopo de Variáveis (LEGB Rule)
Define onde uma variável é acessível. Ordem de busca:

L (Local): Dentro da função atual.
E (Enclosing function locals): Nas funções externas (se aninhadas).
G (Global): Nível principal do script/módulo.
B (Built-in): Nomes pré-definidos do Python (print, len, etc.).
Python

x_global = 10 # G (Global)

def funcao_externa():
  x_enclosing = 20 # E (Enclosing) para funcao_interna

  def funcao_interna():
    x_local = 30 # L (Local)
    print(f"Dentro da interna: x_local={x_local}")
    print(f"Dentro da interna: x_enclosing={x_enclosing}") # Encontra no escopo E
    print(f"Dentro da interna: x_global={x_global}")   # Encontra no escopo G
    # print(len) # Encontraria no escopo B (Built-in)

  print(f"Antes de chamar interna: x_enclosing={x_enclosing}")
  funcao_interna()
  # print(x_local) # Geraria NameError

print(f"Nível global: x_global={x_global}")
funcao_externa()
# print(x_enclosing) # Geraria NameError

# Saída:
# Nível global: x_global=10
# Antes de chamar interna: x_enclosing=20
# Dentro da interna: x_local=30
# Dentro da interna: x_enclosing=20
# Dentro da interna: x_global=10
global keyword
Para modificar uma variável global dentro de uma função. Use com cautela.

Python

contador = 0
def incrementar():
  global contador # Avisa que queremos usar a 'contador' global
  contador += 1
  print(f"Dentro: {contador}")

incrementar()
incrementar()
print(f"Fora: {contador}")
# Saída:
# Dentro: 1
# Dentro: 2
# Fora: 2
nonlocal keyword
Em funções aninhadas, para modificar uma variável do escopo da função externa mais próxima (Enclosing).

Python

def externa():
    x = "original externa"
    def interna():
        nonlocal x # Refere-se ao 'x' da função externa
        x = "modificado pela interna"
        print(f"Interna: {x}")
    interna()
    print(f"Externa após interna: {x}")
externa()
# Saída:
# Interna: modificado pela interna
# Externa após interna: modificado pela interna
Docstrings (Documentation Strings)
String literal ("""Docstring aqui""") como a primeira instrução de uma função/módulo/classe para documentação.

Python

def dividir(numerador, denominador):
  """
  Divide dois números.

  Args:
    numerador: O número a ser dividido (dividendo).
    denominador: O número pelo qual dividir (divisor).

  Returns:
    O resultado da divisão (float).

  Raises:
    ValueError: Se o denominador for zero.
  """
  if denominador == 0:
    raise ValueError("Denominador não pode ser zero!")
  return numerador / denominador

# Acessando a docstring:
# print(dividir.__doc__)
# help(dividir)
Recursão
Uma função que chama a si mesma. Precisa de um caso base para parar.

Python

def fatorial(n):
  """Calcula o fatorial de n (n!) usando recursão."""
  # Caso base: fatorial de 0 ou 1 é 1
  if n == 0 or n == 1:
    return 1
  # Passo recursivo: n! = n * (n-1)!
  else:
    # Comentário: Exibindo a chamada recursiva
    print(f"Calculando {n} * fatorial({n-1})")
    return n * fatorial(n - 1)

resultado_fatorial = fatorial(4) # 4 * 3 * 2 * 1
print(f"Fatorial de 4 é: {resultado_fatorial}")

# Saída:
# Calculando 4 * fatorial(3)
# Calculando 3 * fatorial(2)
# Calculando 2 * fatorial(1)
# Fatorial de 4 é: 24
Nota: Recursão pode ser elegante, mas iteratividade (loops) pode ser mais eficiente em alguns casos.

Funções Lambda (Funções Anônimas)
Pequenas funções inline sem nome formal (def). Sintaxe: lambda argumentos: expressao.

Vários argumentos, mas uma única expressão.
Retorna o valor da expressão implicitamente.
Útil com map, filter, sorted.
Python

# Função lambda
dobrar_lambda = lambda x: x * 2
print(dobrar_lambda(5)) # Saída: 10

somar_lambda = lambda a, b: a + b
print(somar_lambda(3, 4)) # Saída: 7

# Uso com sorted: ordenar pelo segundo elemento da tupla
pontos = [(1, 5), (3, 2), (5, 8), (2, 1)]
pontos_ordenados = sorted(pontos, key=lambda ponto: ponto[1])
print(pontos_ordenados) # Saída: [(2, 1), (3, 2), (1, 5), (5, 8)]

# Uso com map: aplicar a cada item
numeros = [1, 2, 3, 4]
quadrados = list(map(lambda n: n ** 2, numeros))
print(quadrados) # Saída: [1, 4, 9, 16]

# Uso com filter: filtrar itens
pares = list(filter(lambda n: n % 2 == 0, numeros))
print(pares) # Saída: [2, 4]
Funções como Objetos de Primeira Classe
Funções são objetos como quaisquer outros em Python:

Podem ser atribuídas a variáveis.
Podem ser passadas como argumentos.
Podem ser retornadas de outras funções.
Python

def dizer_ola(nome):
  return f"Olá, {nome}!"

def dizer_tchau(nome):
  return f"Tchau, {nome}!"

# 1. Atribuir a uma variável
saudacao = dizer_ola
print(saudacao("Pedro")) # Saída: Olá, Pedro!

# 2. Passar como argumento
def executar_saudacao(funcao_saudacao, nome_pessoa):
  print(funcao_saudacao(nome_pessoa))

executar_saudacao(dizer_ola, "Joana")   # Saída: Olá, Joana!
executar_saudacao(dizer_tchau, "Lucas") # Saída: Tchau, Lucas!

# 3. Retornar uma função
def escolher_saudacao(manha):
  if manha:
    return dizer_ola
  else:
    return dizer_tchau

saudacao_da_manha = escolher_saudacao(True)
saudacao_da_tarde = escolher_saudacao(False)

print(saudacao_da_manha("Sol")) # Saída: Olá, Sol!
print(saudacao_da_tarde("Lua")) # Saída: Tchau, Lua!
Decoradores (Conceito Avançado)
"Embrulham" funções para adicionar funcionalidades extras sem modificar o código original. Sintaxe: @decorator.

Python

import time

# Função decoradora
def medir_tempo(func):
  """Decorador que mede o tempo de execução de uma função."""
  def wrapper(*args, **kwargs):
    inicio = time.time()
    resultado = func(*args, **kwargs) # Chama a função original
    fim = time.time()
    # Comentário: Exibe o tempo de execução
    print(f"[Função '{func.__name__}' levou {fim - inicio:.6f}s]")
    return resultado
  return wrapper

# Aplicando o decorador
@medir_tempo
def processo_demorado(n):
  """Simula um processo que leva algum tempo."""
  soma = 0
  for i in range(n):
    soma += i
  time.sleep(0.1) # Simula trabalho
  return soma

@medir_tempo
def outra_funcao(a, b):
  time.sleep(0.05)
  return a + b

soma1 = processo_demorado(100000)
print(f"Resultado processo_demorado: {soma1}")

soma2 = outra_funcao(5, 10)
print(f"Resultado outra_funcao: {soma2}")

# Saída (o tempo exato pode variar):
# [Função 'processo_demorado' levou 0.104587s]
# Resultado processo_demorado: 4999950000
# [Função 'outra_funcao' levou 0.050123s]
# Resultado outra_funcao: 15
Boas Práticas
Nomes Claros: Use nomes descritivos (verbos/ações).
Tamanho: Funções curtas, fazendo uma coisa bem feita (SRP).
Docstrings: Sempre documente suas funções.
Type Hints: Use anotações de tipo (ex: def soma(a: int, b: int) -> int:).
Evite Efeitos Colaterais: Minimize modificações de estado fora da função.