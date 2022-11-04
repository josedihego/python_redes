
import socket
host = 'localhost'
port = 1600

# Cria socket TCP/IP
socket_cliente = socket.socket(socket.AF_INET,
                               socket.SOCK_STREAM)
# Conecta o socket cm o servidor
endereco_servidor = (host, port)
print('Conectando ao %s na porta %s' %
      endereco_servidor)
socket_cliente.connect(endereco_servidor)

# Envio de mensagens
try:
    # Senvio da mensagem
    message = 'Mensagem de teste.'
    # substiuir essa mensagem com o nome do SO
    print('Enviando %s' % message)
    socket_cliente.sendall(message.encode('utf-8'))
    # Aguardando resposta
    total_recebido = 0
    quantidade_esperada = len(message)
    while total_recebido < quantidade_esperada:
        dados = socket_cliente.recv(16)
        total_recebido = total_recebido+ len(dados)
        print('Recebidos do servidor: %s' % dados)
except socket.error as erro:
    print('Erro de socket: %s' % str(erro))
except Exception as erro:
    print('Outro erro: %s' % str(erro))
finally:
    print('Encerrando conexão com servidor')
    socket_cliente.close()
