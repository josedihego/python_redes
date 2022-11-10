# PROBLEMAS
# Senhas e arquivos são enviados sem qualquer proteção
# ataques: man-in-the-middle
# alternativas: SFTP, SSH (Secure Shell), HTTPS e web servers
# FTP usa conexões longas se comparadas ao HTTP, curtas e pontuais
# Unix/Linux: VSFTPD (Very Secure File Transfer Protocol Daemon)
# Windows/Mac/Linux: FileZilla

from pyftpdlib.authorizers import DummyAuthorizer
# - DummyAuthorizer gerencia autenticações e permissões do servidor FTP
# - senhas salvas sem qualquer proteção em arquivos de texto
#  - serve como base para criação de gerenciadores de autorização mais complexos
# - usado dentro de um ...
from pyftpdlib.handlers import FTPHandler
# - FTPHandler para verificar usuário e senha,
# - acessar diretório de trabalho
# - checar permissões de leitura e escrita
from pyftpdlib.servers import FTPServer
# - FTPServer: servidor FTP


autoridade = DummyAuthorizer()
autoridade.add_user(
    'admin', 'admin', '/home/josedihego/servidorFTP/', perm='elradfmw')
autoridade.add_user('patativa', 'p34f2', '/home/josedihego/servidorFTP/', perm='elradfmw')

gerenteFTP = FTPHandler
gerenteFTP.authorizer = autoridade

servidor = FTPServer(('10.25.120.246', 1026), gerenteFTP)
servidor.serve_forever()

# permissões
# "e" = mudar diretório (CWD, CDUP )
# "l" = listar arquivos (LIST, NLST, STAT, MLSD, MLST, SIZE )
# "r" = baixar arquivos (RETR)
# "a" = adicionar dados a um arquivo existente (APPE )
# "d" = remover um arquivo ou diretório (DELE, RMD)
# "f" = renomear um arquivo ou diretório (RNFR, RNTO )
# "m" = criar um diretório (MKD )
# "w" = armazenar um arquivo no servidor (STOR, STOU )
# "M" = mudar as permissões de um arquivo (SITE CHMOD )
# "T" = mudar o tempo do arquivo (SITE MFMT )
