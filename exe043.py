peso = float (input ('Entre com seu peso: '))
alt = float (input ('Entre com sua altura em m: '))
imc = peso / (alt ** 2)
if imc < 18.5:
    print ('Seu IMC é {:.2f} e você está ABAIXO DO PESO IDEAL'.format (imc))
elif imc >= 18.5 and imc < 25:
    print ('Seu IMC é {:.2f} e você está com o PESO IDEAL'.format (imc))
elif imc >= 25 and imc < 30:
    print ('Seu IMC é {:.2f} e você está com SOBREPESO'.format (imc))
elif imc >= 30 and imc < 40:
    print ('Seu IMC é {:.2f} e você está com OBESIDADE'.format (imc))
else:
    print ('Seu IMC é {:.2f} e você está com OBESIDADE MÓRBIDA'.format (imc))
