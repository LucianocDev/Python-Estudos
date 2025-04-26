#Dicionario e seus metodos

meu_dicionario = {'nome': 'João', 'idade': 25, 'cidade': 'São Paulo'}  

# Adicionando um novo par chave-valor
meu_dicionario['profissao'] = 'Engenheiro'

# Atualizando o valor de uma chave existente
meu_dicionario['idade'] = 26

# Removendo um par chave-valor
del meu_dicionario['cidade']

# Obtendo o valor de uma chave
nome = meu_dicionario['nome']

# Verificando se uma chave existe no dicionário
if 'idade' in meu_dicionario:
    print("A chave 'idade' existe no dicionário.")

# Obtendo todas as chaves do dicionário
chaves = meu_dicionario.keys()

# Obtendo todos os valores do dicionário
valores = meu_dicionario.values()

# Obtendo todos os pares chave-valor do dicionário
pares_chave_valor = meu_dicionario.items()

# Obtendo o comprimento do dicionário
comprimento = len(meu_dicionario)

# Limpar o dicionário
meu_dicionario.clear()
print(meu_dicionario)
