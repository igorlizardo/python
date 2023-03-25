import math
cad = float (input ('Valor do cateto adjacente: '))
cop = float (input ('Valor do cateto oposto: '))
hyp = math.hypot (cop , cad)
print ('A hipotenusa tem o comprimento de {:.2f}'.format (hyp))

