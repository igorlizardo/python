n1 = int (input ('Digite um número: '))
n2 = int (input ('Digite outro número: '))
if n2<n1:
    maior = n1
    print ('O maior número é {} e o menor número é {}'.format (maior , n2))
elif n2>n1:
    maior = n2
    print ('O maior número é {} e o menor número é {}'.format (maior , n1))
else:
    print ('Os números são iguais!')

