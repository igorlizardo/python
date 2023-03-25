import random
j1 = str (input ('Pedra, Papel ou Tesoura? '))
pe = 'pedra'
pa = 'papel'
te = 'tesoura'
lista = [pe , pa , te]
comp = random.choice (lista)
if j1 == comp:
    print ('Jogador 1 escolheu {} e computador escolheu {}. Empate!'.format (j1 , comp))
elif j1 == 'pedra' and comp == pa:
    print ('O jogador 1 escolheu {} e o computador escolheu {}, sendo assim o vencedor foi Computador!'.format (j1 , comp))
elif j1 == 'papel' and comp == pe:
    print ('O jogador 1 escolheu {} e o computador escolheu {}, sendo assim o vencedor foi Jogador 1!'.format (j1 , comp))
elif j1 == 'pedra' and comp == te:
    print ('O jogador 1 escolheu {} e o computador escolheu {}, sendo assim o vencedor foi Jogador 1!'.format (j1 , comp))
elif j1 == 'papel' and comp == te:
    print ('O jogador 1 escolheu {} e o computador escolheu {}, sendo assim o vencedor foi Computador!'.format (j1 , comp))
elif j1 == 'tesoura' and comp == pa:
    print ('O jogador 1 escolheu {} e o computador escolheu {}, sendo assim o vencedor foi Jogador 1!'.format (j1 , comp))
elif j1 == 'tesoura' and comp == pe:
    print ('O jogador 1 escolheu {} e o computador escolheu {}, sendo assim o vencedor foi Computador!'.format (j1 , comp))

