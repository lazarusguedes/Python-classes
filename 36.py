H = int(input('Valor da casa:'))
S = int(input('Salário:'))
Y = int(input('Anos a pagar:'))
M = H/(Y*12)
print(M)
if M>S*0.3:
    print('Infelizmente seu empréstimo não foi aprovado.')
else:
    print('Parabéns, seu empréstimo foi aprovado!')