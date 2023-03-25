frase = str (input ('Digite um frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range (len(junto) - 1, -1 , -1):
    inverso += junto[letra]
if inverso == junto:
    print ('É um PALINDROMO!')
else:
    print ('Não é um PALINDROMO!')
