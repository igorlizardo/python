s = float (input ('\033[mQual é o seu salário? R$\033[32m '))
c = float (input ('\033[mQual é o valor da casa? R$\033[32m '))
t = int (input ('\033[mQual o prazo de financiamento em anos? \033[32m '))
e = float (input ('\033[mQual será sua entrada? R$\033[32m '))
tm = t * 12
p = (c - e) / tm
if p >= (s * 0.3):
    print ('\033[mFinanciamento negado por comprometer mais de 30% do salário.\033[m')
else:
    print ('\033[mSeu financiamento foi aceito! Sua parcela será de R$ \033[32m{:.2f} \033[m!\033[m'.format (p))
