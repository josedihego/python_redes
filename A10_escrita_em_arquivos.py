import datetime

arquivo_log = open('log.txt', 'w')

#
usuario = 'Admin'
arquivo = 'imagem.png'
tipo = 'enviou'
data = datetime.datetime.now()

arquivo_log.write(usuario + ' '+tipo+' '+ arquivo + ' '+ str(data))

arquivo_log.close()