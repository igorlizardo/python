v = int(input ('Digite a velocidade do motorista em km/h: '))
if v > 80:
    print ('Você foi excedeu o limite de 80 km/h e terá que pagar R$ {:.2f}'.format ((v-80)*7))
