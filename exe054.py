from datetime import date
ano = date.today().year
totmaior = 0
totmenor = 0
for pess in range (1 , 8):
    nasc = int (input ('Em que ano a pessoa nasceu: '))
    idade = ano - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor +=1
print ('''Ao todo tivemos {} que atingiram a maior idade 
       e {} que são menores de idade'''.format (totmaior , totmenor))
