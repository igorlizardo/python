d = float (input ('Digite a distância até o destino: '))
print ('-=-' * 20)
if d >= 200:
    print ('Você irá pagar R$ {:.2f} pelo trajeto de {} km'.format ((d*0.45) , d))
else:
    print ('Você irá pagar R$ {:.2f} pelo trajeto de {} km'.format ((d*0.5) , d))
print ('-=-' * 20)
print ('Tenha uma boa viagem!')
