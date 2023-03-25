print ('-=-' * 20)
s = float (input ('\033[mDigite seu salário atual: R$ '))
if s > 1250:
    print ('Seu salário era \033[31mR$ {:.2f}\033[m e com o aumento de 10% passou para \033[32mR$ {:.2f}'.format (s , (s*1.1)))
else:
    print ('Seu salário era R$ {:.2f} e com o aumento de 15% passou para R$ {:.2f}'.format (s , (s*1.15)))
print ('----FIM----')
