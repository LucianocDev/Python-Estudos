# Simulação de função com return
def envia_email():
    email = 'luciano.c.dev@gmail.com'
    senha = '920280'
    email_envio = 'Felipe, Gabriele, Joaozinho'
    # Conecta no provedor
    # Monta o corpo do emila
    # Envia o email
    return 'Email enviado!'

pessoas = ['Felipe', 'Gabriele', 'Joaozinho']
for pessoa in pessoas:
    email_enviado = envia_email()
    print(email_enviado)
