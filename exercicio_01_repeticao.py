import random

n1 = random.randint(1,100)
n2 = random.randint(100,200)
n3 = random.randint(200,300)

nPares = 0

if(n1%2==0):
    nPares = nPares + 1
if(n2%2==0):
    nPares = nPares + 1
if(n3%2==0):
    nPares = nPares + 1

if(nPares >= 2):
    print('Em {}, {}, {} pelo menos dois são pares'.format(n1,n2,n3))
else:
    print('Não foi possivel encontrar dois numeros pares entre {}, {}, {}'.format(n1, n2, n3))