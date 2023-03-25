import random
print ('-=-' * 20)
print ('----Jogo da Adivinhação----')
print ('-=-' * 20)
lista = [1 , 2 , 3 , 4 , 5 , 0]
n1 = random.choice (lista)
n2 = int (input ('Entre com um número de 0 a 5: '))
if n1 == n2:
    print ('Você acertou o número!')
else:
    print ('O número escolhido pelo computador foi {} e você escolheu {}'.format ( n1 , n2))
print ('--FIM--')
