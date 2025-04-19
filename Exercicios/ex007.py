# Simulação de função com entrada de dados
def envia_email(nome, email):       
    nome_destinatario = nome
    email_destinatario = email
    # Conecta no provedor
    # Monta o corpo do emila
    # Envia o email
    
    return f'Email enviado para {nome_destinatario}, dono(a) do email {email_destinatario}'

pessoas = [
    {
        'nome': 'Felipe',
        'email': 'felipe@gmail.com'
    },
    {
        'nome': 'Gabriele',
        'email': 'gabriele@gmail.com'
    },
    {
        'nome': 'Joaozinho',
        'email': 'joaozinho@gmail.com'
    }
]
for pessoa in pessoas:
    email_enviado = envia_email(pessoa['nome'], pessoa['email'])
    print(email_enviado)
    