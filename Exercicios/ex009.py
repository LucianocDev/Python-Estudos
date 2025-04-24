#Exemplo do laço de repetição for
""" Lança um aviso de manutenção de carro """
def carro_manutencao(carro):
    print(f'Programar Manutenção do carro {carro}!')

carros = ['Gol', 'Palio', 'Corsa', 'Uno', 'Celta', 'Fusca', 'Brasilia', 'Fiat 147', 'Fiat Fastback', 'Honda Civic']
for carro in (carros):
    carro_manutencao(carro)
