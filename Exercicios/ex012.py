#Exemplo do laço de repetição for com continue
""" Lança um aviso de manutenção de carro """
def carro_manutencao(carro):
    print(f'Programar Manutenção do carro {carro}!')

carros = ['Gol', 'Palio', 'Corsa', 'Uno', 'Celta', 'Fusca', 'Brasilia', 'Fiat 147', 'Fiat Fastback', 'Honda Civic']
for i, carro in enumerate(carros):
    if i == 4:
        continue
    carro_manutencao(carro)
