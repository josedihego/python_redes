# módulo socket : host local
import socket

nome_host = socket.gethostname()
print('Nome do host: {}'.format(nome_host))
ip_host = socket.gethostbyname(nome_host)
print('Endereço IP: {}'.format(ip_host))

# módulo socket: host remoto

import socket

host_remoto = 'www.python.org'
try:
    ip_host_remoto = socket.gethostbyname(host_remoto)
    print ('endereço IP de {}: {}'.
           format(host_remoto, ip_host_remoto))
except socket.error as msg_erro:
    print ('{}: {}'.format(host_remoto, msg_erro))

# conversão de endereço IPv4 para diferentes formatos
import socket
from binascii import hexlify

for end_ip in ['127.0.0.1', '192.168.0.1']:
    end_ip_byte = socket.inet_aton(end_ip)
    end_ip_original = socket.inet_ntoa(end_ip_byte)
    end_ip_hex = hexlify(end_ip_byte)
    end_ip_binario = bin(int(end_ip_hex,base=16))
    print("Endereço IP: {} => Valor binário: {}".
          format(end_ip_original, end_ip_byte))
    print ("Endereço IP: {} => Hexadecimal: {}".
           format(end_ip_original, end_ip_hex))
    print("Endereço IP: {} => Valor em 0s e 1s: {}".
          format(end_ip_original, end_ip_binario))



# protocolos associados a portas
import socket
nome_protocolo = 'tcp'
for porta in [80, 25, 53]:
    print ("Porta: {} => nome do serviço: {}".
        format(porta,
        socket.getservbyport(porta,
                             nome_protocolo)))

# Acesso a servidor remoto com ntplib
import ntplib
from time import ctime

cliente_ntp = ntplib.NTPClient()
response = cliente_ntp.request('pool.ntp.org')
print (ctime(response.tx_time))