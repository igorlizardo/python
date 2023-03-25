print ('-=-' * 20)
print ('Digite 3 números e veja a ordem do maior para o menor')
print ('-=-' * 20)
n1 = int (input ('Digite um número: '))
n2 = int (input ('Digite um número: '))
n3 = int (input ('Digite um número: '))
menor = n1
maior = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print ('O menor número digitado é {}'.format (menor))
print ('E o maior número digitado é {}'.format (maior))
