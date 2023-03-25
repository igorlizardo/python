frase = str (input ('Digite uma frase: ')).upper().strip()
print ('A frase tem {} letras A'.format(frase.count('A')))
print ('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))
print ('A ultima vez que ela aparece é na posição {}'.format(frase.rfind('A')+1))