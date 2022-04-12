BY = int(input('Ano de Nascimento:'))
CY = int(input('Ano atual:'))
I = CY-BY
II = 18-I
III = I-18
if I<18:
    print('Ainda não chegou sua hora.')
    print(f'Faltam {II} anos.')
elif I==18:
    print('Que os jogos comecem.')
else:
    print('Já passou da hora, soldado!')
    print(f'Já passaram {III} anos!')