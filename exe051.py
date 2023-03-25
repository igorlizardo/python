primeiro = int (input ('Digite o primeiro termo: '))
razão = int (input ('Digite a razão: '))
n = int (input ('Digite o enésimo termo da PA: '))
en = primeiro + (n - 1) * razão
for c in range (primeiro , en , razão):
    print ('{} '.format (c), end = ' ')
print ('ACABOU')
