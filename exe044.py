valor = float (input ('Qual o valor do produto: R$ '))
pg = str (input ('Qual a forma de pagamento: '))
if pg == 'dinheiro' or pg == 'cheque':
    print ('O valor a ser pago é de R$ {:.2f}'.format ((valor - (valor * 0.1))))
elif pg == 'cartão':
    vzs = int (input ('Quantas vezes você irá dividir? '))
    if vzs == 1:
        print ('Você irá pagar R$ {:.2f}'.format ((valor - (valor * 0.05))))
    elif vzs == 2:
        print ('Você irá pagar um total de R$ {:.2f} em 2 parcelas de R$ {:.2f}'.format (valor , (valor / 2)))
    else:
        print ('Você irá pagar um total de R$ {:.2f} em {} parcelas de R$ {:.2f}'.format ((valor + (valor * 0.2)) , vzs , ((valor + (valor * 0.2)) / vzs)))
else:
    print ('OPÇÃO INVÁLIDA DE PAGAMENTO')

               