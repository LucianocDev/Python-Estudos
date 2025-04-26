#Exemplo de lista dentro de dicionario
carros = {
    'marca': 'Fiat',
    'modelo': 'Uno',
    'ano': 2015,
    'cor': 'Preto',
    'motor': ['1.0', '1.4', '1.6', '1.8'],
    'Opcionais': ['Ar Condicionado', 'Direção Elétrica', 'Câmbio Automático', 'Roda de Liga Leve'],
    'Preço': 30000,
    'Acessórios': ['Câmera de Ré', 'Banco de Couro', 'Banco de Couro']
}
print(carros['Opcionais'][1])
