from datetime import date
ano = date.today().year
nasc = int (input ('Digite o ano de nascimento do atleta: '))
id = (ano - nasc)
if id <= 9:
    print ('Atleta categoria MIRIM')
elif id >9 and id <=14:
    print ('Atleta categoria INFANTIL')
elif id > 14 and id <= 19:
    print ('Atleta categoria JÚNIOR')
elif id > 19 and id <= 25:
    print ('Atleta categoria SÊNIOR')
else:
    print ('Atleta categoria MASTER')
