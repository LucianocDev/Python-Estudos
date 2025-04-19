# Função para calcular exponenciação

def potencia(base, expoente):
    """Calcula a potenciação de um número"""
    return base ** expoente

# Exemplo de uso da função
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))
resultado = potencia(base, expoente)
print(f"{base} elevado a {expoente} é igual a {resultado}")
