I = float(input('Primeira Nota:'))
II = float(input('Segunda Nota:'))
A = (I+II)/2
if A<5:
    print('Reprovado')
elif A<6.9:
    print('Recuperação')
else:
    print('Aprovado')