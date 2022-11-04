# https://github.com/PacktPublishing/Python-Network-Programming-Cookbook-Second-Edition

import socket
host = '10.25.120.70'
payload_dados = 2048
tamanho_fila = 5
porta = 1600

# Criação de socket
socket_servidor = socket.socket(socket.AF_INET,
                                socket.SOCK_STREAM)
# Habilitando reuso de endereço e porta
socket_servidor.setsockopt(socket.SOL_SOCKET,
                           socket.SO_REUSEADDR, 1)
# Ligando o socket com a porta
endereco_servidor = (host, porta)
print('Iniciando o servidor %s na porta %s'
      % endereco_servidor)
socket_servidor.bind(endereco_servidor)
# Aguardando clientes.tamanho_fila especifica
# o tamanho máximo da fila de clientes
socket_servidor.listen(tamanho_fila)
# ler o valor de n
# definir um contador de cliente
while True: # modificar o True, substituindo pela verificação de n
    # cada vez que entrar no while faz o contador receber contador +1
    print('Esperando mensagens do cliente')
    cliente, end_cliente = socket_servidor.accept()
    dados = cliente.recv(payload_dados)
    # fazer o seu if elif e else
    if dados:
        print('Dados: %s' % dados)
        cliente.send(dados)
        print('enviado %s bytes de volta para %s'
              % (dados, end_cliente))
    # end connection
    cliente.close()