# Dicionários Python: Um Guia Detalhado

Exercicios ex016, ex017, ex018 (pasta de exercicios).

Os dicionários em Python, conhecidos como `dict`, são estruturas de dados fundamentais e flexíveis que permitem armazenar coleções de itens de forma organizada. Diferente de listas ou tuplas que são indexadas por números, os dicionários são indexados por chaves únicas e imutáveis (como strings, números ou tuplas contendo apenas tipos imutáveis). Cada chave é associada a um valor, formando pares chave-valor. Essa estrutura é frequentemente utilizada para representar objetos ou relações do mundo real, onde cada chave representa um atributo e seu valor correspondente.

## Criação de Dicionários

Existem duas formas principais de criar dicionários em Python:

1.  **Usando chaves `{}`**: Esta é a forma mais comum. Os pares chave-valor são inseridos entre chaves, separados por vírgulas, com a chave e o valor de cada par separados por dois-pontos `:`.
    ```
    # Dicionário representando uma pessoa
    pessoa = {"nome": "Alice", "idade": 25, "cidade": "São Paulo"}
    print(pessoa)
    # Output: {'nome': 'Alice', 'idade': 25, 'cidade': 'São Paulo'}

    # Dicionário vazio
    dict_vazio = {}
    print(dict_vazio)
    # Output: {}
    ```

2.  **Usando a função `dict()`**: Esta função construtora pode ser usada para criar dicionários. Ao usar argumentos nomeados, os nomes dos argumentos se tornam as chaves (obrigatoriamente como strings) e os valores dos argumentos se tornam os valores do dicionário.
    ```
    # Criando um dicionário usando dict() com argumentos nomeados
    carro = dict(marca="Chevrolet", modelo="Tracker", ano=2020)
    print(carro)
    # Output: {'marca': 'Chevrolet', 'modelo': 'Tracker', 'ano': 2020}
    ```
    A função `dict()` também pode converter outras estruturas (como listas de tuplas) em dicionários.

## Acesso a Elementos

Para acessar o valor associado a uma chave específica, utiliza-se a sintaxe de colchetes `[]` com a chave desejada.
pessoa = {"nome": "Alice", "idade": 25}
nome_pessoa = pessoa['nome']
print(nome_pessoa) # Output: Alice

text
Se a chave especificada não existir no dicionário, tentar acessá-la com `[]` resultará em um erro (`KeyError`). Para evitar isso, pode-se usar o método `get()`.

### Método `get()`
O método `get(chave, valor_padrao)` retorna o valor associado à `chave`. Se a chave não for encontrada, ele retorna `None` por padrão, ou o `valor_padrao` especificado, sem gerar erro.
pessoa = {"nome": "Bob", "idade": 30}

Acessando chave existente
idade = pessoa.get("idade")
print(idade) # Output: 30

Tentando acessar chave inexistente sem valor padrão
profissao = pessoa.get("profissao")
print(profissao) # Output: None

Tentando acessar chave inexistente com valor padrão
cidade = pessoa.get("cidade", "Não especificado")
print(cidade) # Output: Não especificado

text

## Adição e Modificação de Elementos

Adicionar um novo par chave-valor ou modificar o valor de uma chave existente é feito através de atribuição direta usando colchetes `[]`.
pessoa = {'nome': 'Carlos', 'idade': 30}

Modificando um valor existente
pessoa['idade'] = 31
print(pessoa) # Output: {'nome': 'Carlos', 'idade': 31}

Adicionando um novo par chave-valor
pessoa['profissao'] = 'Engenheiro'
print(pessoa) # Output: {'nome': 'Carlos', 'idade': 31, 'profissao': 'Engenheiro'}

text

### Método `update()`
O método `update()` permite adicionar múltiplos pares chave-valor de outro dicionário (ou de um iterável de pares chave-valor) ao dicionário atual. Se chaves existentes forem fornecidas, seus valores serão atualizados.
meu_dicionario = {"nome": "Alice", "idade": 25}
print("Original:", meu_dicionario)

Atualizando 'idade' e adicionando 'cidade'
meu_dicionario.update({"idade": 26, "cidade": "São Paulo"})
print("Atualizado:", meu_dicionario)

Output:
Original: {'nome': 'Alice', 'idade': 25}
Atualizado: {'nome': 'Alice', 'idade': 26, 'cidade': 'São Paulo'}
text

## Remoção de Elementos

Existem várias formas de remover elementos de um dicionário:

*   **Método `pop()`**: Remove o item com a chave especificada e retorna o seu valor. Se a chave não existir, gera um `KeyError`, a menos que um valor padrão seja fornecido como segundo argumento.
    ```
    pessoa = {'nome': 'Carlos', 'idade': 31, 'profissao': 'Engenheiro'}
    idade_removida = pessoa.pop('idade')
    print(f"Idade removida: {idade_removida}") # Output: Idade removida: 31
    print(pessoa) # Output: {'nome': 'Carlos', 'profissao': 'Engenheiro'}

    # Removendo chave inexistente com valor padrão
    valor_removido = pessoa.pop('salario', 'Chave não encontrada')
    print(valor_removido) # Output: Chave não encontrada
    ```
*   **Método `popitem()`**: Remove e retorna o último par chave-valor inserido no dicionário (em versões Python 3.7+). Em versões anteriores, remove um par arbitrário.
    ```
    pessoa = {'nome': 'Carlos', 'profissao': 'Engenheiro'}
    ultimo_item = pessoa.popitem()
    print(f"Último item removido: {ultimo_item}") # Output: Último item removido: ('profissao', 'Engenheiro')
    print(pessoa) # Output: {'nome': 'Carlos'}
    ```
*   **Palavra-chave `del`**: Remove o item com a chave especificada. Não retorna o valor.
    ```
    pessoa = {'nome': 'Carlos', 'cidade': 'Rio'}
    del pessoa['cidade']
    print(pessoa) # Output: {'nome': 'Carlos'}
    ```
    `del` também pode ser usado para remover o dicionário inteiro.
*   **Método `clear()`**: Remove *todos* os itens do dicionário, deixando-o vazio.
    ```
    pessoa = {'nome': 'Ana', 'idade': 28}
    pessoa.clear()
    print(pessoa) # Output: {}
    ```

## Métodos Comuns de Dicionários

Python oferece vários métodos úteis para trabalhar com dicionários:

*   **`keys()`**: Retorna uma "visão" (um objeto do tipo `dict_keys`) contendo todas as chaves do dicionário. Essa visão é dinâmica, refletindo alterações no dicionário. Pode ser convertida em lista se necessário.
    ```
    meu_dicionario = {"nome": "Eva", "idade": 24, "profissão": "Engenheira"}
    chaves = meu_dicionario.keys()
    print(chaves) # Output: dict_keys(['nome', 'idade', 'profissão'])
    print(list(chaves)) # Output: ['nome', 'idade', 'profissão']
    ```
*   **`values()`**: Retorna uma visão (`dict_values`) contendo todos os valores do dicionário. Também é dinâmica.
    ```
    meu_dicionario = {"nome": "Eva", "idade": 24, "profissão": "Engenheira"}
    valores = meu_dicionario.values()
    print(valores) # Output: dict_values(['Eva', 24, 'Engenheira'])
    print(list(valores)) # Output: ['Eva', 24, 'Engenheira']
    ```
*   **`items()`**: Retorna uma visão (`dict_items`) contendo tuplas, onde cada tupla é um par (chave, valor) do dicionário. É muito útil para iteração.
    ```
    meu_dicionario = {"nome": "Eva", "idade": 24, "profissão": "Engenheira"}
    itens = meu_dicionario.items()
    print(itens) # Output: dict_items([('nome', 'Eva'), ('idade', 24), ('profissão', 'Engenheira')])
    print(list(itens)) # Output: [('nome', 'Eva'), ('idade', 24), ('profissão', 'Engenheira')]
    ```
*   **`copy()`**: Retorna uma cópia *superficial* (shallow copy) do dicionário. Modificações no dicionário original não afetarão a cópia, e vice-versa, a menos que os valores sejam objetos mutáveis (como listas), que ainda serão compartilhados.
    ```
    original = {'a': 1, 'b':}
    copia = original.copy()
    copia['a'] = 100
    copia['b'].append(4)

    print(f"Original: {original}") # Output: Original: {'a': 1, 'b':}
    print(f"Cópia: {copia}")     # Output: Cópia: {'a': 100, 'b':}
    ```

## Iteração em Dicionários

É possível percorrer (iterar sobre) as chaves, valores ou pares chave-valor de um dicionário usando um loop `for` em conjunto com os métodos `keys()`, `values()` e `items()`.

funcionario = {"nome": "Pedro", "sobrenome": "Silva", "salario": 6500}

Iterando sobre as chaves (comportamento padrão ao iterar diretamente no dicionário)
print("--- Chaves ---")
for chave in funcionario: # ou funcionario.keys()
print(f'Chave -> {chave}')

Iterando sobre os valores
print("\n--- Valores ---")
for valor in funcionario.values():
print(f'Valor -> {valor}')

Iterando sobre os pares chave-valor
print("\n--- Itens (Chave-Valor) ---")
for chave, valor in funcionario.items():
print(f'Chave "{chave}" associada ao valor "{valor}"')

text
Saída:
--- Chaves ---
Chave -> nome
Chave -> sobrenome
Chave -> salario

--- Valores ---
Valor -> Pedro
Valor -> Silva
Valor -> 6500

--- Itens (Chave-Valor) ---
Chave "nome" associada ao valor "Pedro"
Chave "sobrenome" associada ao valor "Silva"
Chave "salario" associada ao valor "6500"

text
Note que na iteração sobre `items()`, usamos desempacotamento de tuplas (`chave, valor`) para acessar diretamente a chave e o valor em cada iteração.

## Outras Operações Comuns

*   **Verificar existência de chave**: Use o operador `in`.
    ```
    pessoa = {"nome": "Ana"}
    print('nome' in pessoa)  # Output: True
    print('idade' in pessoa) # Output: False
    ```
*   **Obter o tamanho**: Use a função `len()` para saber quantos pares chave-valor o dicionário possui.
    ```
    pessoa = {"nome": "Ana", "idade": 28}
    print(len(pessoa)) # Output: 2
    ```
*   **Dicionários Aninhados**: Dicionários podem conter outros dicionários como valores, permitindo estruturas de dados complexas.
    ```
    familia = {
        'pai': {'nome': 'Roberto', 'idade': 50},
        'mãe': {'nome': 'Marta', 'idade': 48},
        'filho': {'nome': 'Carlos', 'idade': 31}
    }
    print(familia['pai']['nome']) # Output: Roberto
    ```
*   **Transformar Lista em Dicionário**: Pode-se criar um dicionário a partir de uma lista, geralmente iterando sobre a lista e adicionando pares chave-valor com base em alguma lógica.
    ```
    palavras = ["python", "asimov", "academy"]
    dict_palavras = {}
    for palavra in palavras:
        dict_palavras[palavra] = len(palavra) # Chave: palavra, Valor: tamanho da palavra
    print(dict_palavras)
    # Output: {'python': 6, 'asimov': 6, 'academy': 7}
    ```

Os dicionários são ferramentas extremamente versáteis em Python, ideais para armazenar e gerenciar dados de forma eficiente e legível.