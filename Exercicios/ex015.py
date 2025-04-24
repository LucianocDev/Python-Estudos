# Exemplo do laço de repetição while com continue
""" Imprime números de 1 a 10 """
numero = 0
while numero <= 10:
    if numero == 5:
        numero += 1
        continue
    print(numero)
    numero += 1
    