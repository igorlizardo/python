n = int (input ('\033[mDigite um número: '))
tot = 0
for c in range (1 , n + 1):
    if n % c == 0:
        print ('\033[33m', end = '  ')
        tot = tot + 1
    else:
        print ('\033[31m', end = '  ')
    print ('{}'.format (c), end = '  ')
print ('\n\033[mO número {} foi divisível {} vezes'.format (n , tot))
if tot == 2:
    print ('Esse número é primo!')
else:
    print ('Ele não é primo')
