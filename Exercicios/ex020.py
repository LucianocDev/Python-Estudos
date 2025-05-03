#Exemplo de compreensão de listas

numeros = [1, 2, 3, 4, 5]

def dobro(numero):
    return numero * 2
numeros_dobrados = [dobro(numero) for numero in numeros]

print(numeros_dobrados)
