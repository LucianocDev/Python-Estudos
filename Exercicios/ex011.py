#Exemplo do laço de repetição for break
""" Lança um aviso de manutenção de carro """
def carro_manutencao(carro):
    print(f'Programar Manutenção do carro {carro}!')

carros = ['Gol', 'Palio', 'Corsa', 'Uno', 'Celta', 'Fusca', 'Brasilia', 'Fiat 147', 'Fiat Fastback', 'Honda Civic']
for i, carro in enumerate(carros):
    if i == 5:
        break
    carro_manutencao(carro)
