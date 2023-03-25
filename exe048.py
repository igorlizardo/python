soma = 0
cont = 0
for c in range (1 , 500):
    n = c % 3
    if n == 0 and n != c % 2 :
        cont = cont +1
        soma = soma + c
print ('A soma dos {} números que são múltiplos de 3 é {}'.format (cont , soma))        
 