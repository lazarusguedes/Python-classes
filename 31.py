D = float(input('Distância:'))
I = D*0.5
II = D*0.45
if D<=200:
    print(f'Valor da Multa:{I}R$')
else:
    print(f'Valor da Multa:{round(II)}R$')