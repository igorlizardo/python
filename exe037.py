num = int (input ('Qual é o número? '))
print ('''Escolha uma das bases para conversão:
       [1] converter para BINÁRIO
       [2] converter para OCTAL
       [3] converter para HEXADECIMAL''')
opção = int (input (' Sua opção: '))
if opção == 1:
    print ('Seu número em BINÁRIO é {}'.format (bin(num)[2:]))
elif opção == 2:
    print ('Seu número em OCTAL é {}'.format (oct(num)[2:]))
else:
    print ('Seu número em HEXADECIMAL é {}'.format (hex(num)[2:]))

