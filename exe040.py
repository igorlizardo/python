n1 = float (input ('Digite a primeira nota: '))
n2 = float (input ('Digite a segunda nota: '))
md = (n1 + n2) / 2
if md <= 5.0:
    print ('Sua média foi {:.2f} e é inferior à 5.0, portanto você está REPROVADO!'.format (md))
elif md > 5.0 and md <= 6.9:
    print ('Sua média foi {:.2f} e você está de RECUPERAÇÃO!'.format (md))
else:
    print ('Você teve uma média {:.2f} e foi você está APROVADO'.format (md))
