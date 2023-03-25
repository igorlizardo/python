s = float (input ('Digite qual é o seu salário: R$ '))
a = float (input ('Aumento a ser dado em %: '))
print ('Meu salário anterior era R$ {:.2f} e após o aumento de {} %, o novo salário será de R$ {:.2f} '.format ( s , a , (s*(1+(a/100)))))
