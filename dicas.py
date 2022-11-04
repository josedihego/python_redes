
numero_clientes = int(input('Informe o número de clientes: '))
contador = 0
total_win = 0
total_linux = 0
total_mac = 0
total_ourtros = 0
while(contador < numero_clientes):
    contador = contador + 1
    # faça alguma coisa aqui dentro
    print('contador = {}'.format(contador))
    mensagem_do_cliente =  'Windows'
    if(mensagem_do_cliente == 'Windows'):
        total_win = total_win + 1
    elif(mensagem_do_cliente == 'Linux'):
        total_linux = total_linux + 1
    elif(mensagem_do_cliente=='mac'):
        total_mac =  total_mac +1
    else:
        total_outros = total_outros + 1