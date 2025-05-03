# Exemplo de compreensão de listas com condicional

nomes = ['Ana', 'luciano', 'juliano', 'naara', 'theo']
nomes_maiusculos = [nome.upper() for nome in nomes if nome[0] == 'l']

print(nomes_maiusculos)
