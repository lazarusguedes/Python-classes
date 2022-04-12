P = float(input('Preço:'))
M = input('Meio de Pagamento:')
I = P*0.9
II = P*0.95
III = P*1.2
if M == 'dinheiro' or M == 'cheque':
    print(I)
elif M == '1x':
    print(II)
elif M == '2x':
    print(P)
else:
    print(III)
