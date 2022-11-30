# -*- coding: utf-8 -*-

from ftplib import FTP

# ftplib: implementação protocilo FTP cliente

ftp = FTP('')
# criação de um objeto FTP
ftp.connect('10.25.120.94', 1026)
# conexão ao servidor FTP
ftp.login('patativa', 'p34f2')
# login no servidor com usuário e senha
ftp.cwd('/')


# navegação no diretório do usuário

def enviarArquivo():
    nome_arquivo = input('Informe o nome do arquivo:')
    ftp.storbinary('STOR ' + nome_arquivo, open(nome_arquivo, 'rb'))
    # armazena arquivo remotamente no servidor FTP em modo binário de leitura


def baixarArquivo():
    nome_arquivo = input('Informe o nome do arquivo:')
    arquivo_local = open(nome_arquivo, 'wb')
    # abre arquivo em modo binário de escrita
    ftp.retrbinary('RETR ' + nome_arquivo, arquivo_local.write, 1024)
    arquivo_local.close()


def criarDiretorio():
    nome_diretorio = input('informe o nome do novo diretório: ')
    ftp.mkd(nome_diretorio)


def removerDiretorio():
    nome_diretorio = input('informe o nome do diretório a ser removido: ')
    ftp.rmd(nome_diretorio)


def removerArquivo():
    nome_arquivo = input('informe o nome do arquivo a ser removido: ')
    ftp.delete(nome_arquivo)


def renomearArquivo():
    nome_atual = input('informe o nome atual do  arquivo: ')
    nome_novo = input('informe o novo nome do  arquivo: ')
    ftp.rename(nome_atual, nome_novo)


opcao = 0
while (opcao != 1):
    print('Informe uma das opções')
    print('\t 1. sair')
    print('\t 2. listar arquivos')
    print('\t 3. enviar arquivo')
    print('\t 4. baixar arquivo')
    print('\t 5. deletar arquivo')
    print('\t 6. criar diretório')
    print('\t 7. deletar diretório')
    print('\t 8. renomear arquivo')
    opcao = int(input())
    if opcao == 1:
        ftp.quit()
    elif opcao == 2:
        ftp.retrlines('LIST')
    elif opcao == 3:
        enviarArquivo()
    elif opcao == 4:
        baixarArquivo()
    elif opcao == 5:
        removerArquivo()
    elif opcao == 6:
        criarDiretorio()
    elif opcao == 7:
        removerDiretorio()
    elif opcao == 8:
        renomearArquivo()
