print('-=-' * 30)
print ('Analisador de Triângulos')
print('-=-' * 30)
t1 = float (input ('Primeiro segmento: '))
t2 = float (input ('Segundo segmento: '))
t3 = float (input ('Terceiro segmento: '))
if t1 < t2 + t3 and t2 < t3 + t1 and t3 < t2 + t1:
    print ('A soma dos segmentos formam um Triângulo!')
    if t1 == t2 and t2 == t3:
        print ('Esse triângulo é EQUILÁTERO!')
    elif t1 == t2 and t2 != t3 or t1 == t3 and t3 != t2:
        print ('Este triângulo é ISÓSCELES!')
    else:
        print ('Este triângulo é ESCALENO!')
else:
    print ('Não formam um Triângulo!')
