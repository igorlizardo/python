from datetime import date
ano = int (input ('Que ano você deseja analisar? Coloque 0 se deseja analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print ('Esse ano é BISSEXTO!!')
else:
    print ('Esse ano NÃO é BISSEXTO!!!')
print ('-=-' * 20)



        