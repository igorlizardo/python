from datetime import date
ano = date.today().year
nasc = int (input('Digite o ano do seu nascimento: '))
if (ano - nasc) < 18:
    print ('Ainda irá se alistar!')
elif (ano - nasc) == 18:
    print ('Está na hora de se alistar!')
else:
    print ('Já passou do tempo de se alistar!')
