p = float (input ('Digite o valor do produto: R$ '))
d = float (input ('Digite o desconto a ser dado em %: '))
print ('O valor do produto é R$ {:.2f} e o desconto será de {} %, assim o novo valor será de R$ {:.2f} '.format ( p , d, (p*(1-(d/100)))))
