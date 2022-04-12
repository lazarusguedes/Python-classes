A=0
B=0
for c in range(0,2):
    M=input('Nome:')
    N=int(input('Ano de nascimento:'))
    if 2022-N<18:
        print('Menor de idade')
        A=A+1
    else:
        print(('Maior de Idade'))
        B=B+1
print(f'Maiores de idade:{A}')
print(f'Menores de Idade:{B}')
