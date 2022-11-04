n1 = input('Informe o primeiro número: ')
n2 = input('Informe o segundo número: ')
n3 = input('Informe o terceiro número: ')

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

qntPares  = 0

if(n1%2==0):
   qntPares = qntPares +1
if(n2%2==0):
    qntPares = qntPares + 1
if(n3%2==0):
    qntPares = qntPares +1

if(qntPares >=2) :
    print('Encontrei pelo menos dois números pares')
else:
    print('Não encontrei dois números pares')