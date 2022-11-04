# tipo Booleano: True, False

porta_fechada = True
print('Porta fechada? {}'.format(porta_fechada))

sistema_on =  True
servidor_on  =  False
sistema_e_servidor_on  =  sistema_on and servidor_on
print('Sistema E servidor estão on? {}'.
      format(sistema_e_servidor_on))
# operações: or, and, not

# tipos numéricos :  int, float, complex

x = 15.0
y = 4.0

a = x+y
b = x * y
c = x / y
d = x// y
e = x% y
f =  divmod(x,y)
g = pow(x,y)
print('x+y = {}'.format(a))
print('x*y = {}'.format(b))
print('x / y = {}'.format(c))
print('x // y = {}'.format(d))
print('x %y  = {}'.format(e))
print('divmod(x,y)= {}'.format(f))
print('pow(x,y)= {}'.format(g))

# Tipos sequencias:  list, tuple, range

nomes  = ['Maria', 'Alice', 'João', 'Antônio', 'Leila', 'Ana']
print('Maria' in nomes)
print(nomes[2])
print(nomes[2:4])
print(len(nomes))
print(min(nomes))
print(max(nomes))

# Tipos str (texto)

frase = 'Posso não concordar com suas idéias' \
        'mas defenderei o direito que você' \
        'as diga até a morte'
print('concordar' in frase)
print(frase.upper())
print(frase.lower())



