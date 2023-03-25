km = float (input ('Qual a km rodada? '))
dia = int (input ('Quantas diarias foram utilizadas? '))
total = (km * 0.15) + (dia * 60)
print ('O total a ser pago pela locação é de R$ {:.2f}'.format (total))