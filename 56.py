A=0
B=0
C=[]
D=0
for c in range(0,2):
    Name=input('Nome:')
    Age=float(input('Idade:'))
    Sex=input('Sexo:')
    A+=Age
    if Sex =='girl' and Age<20:
        B=B+1
    if Sex=='boy':
        C.insert(0,Age)
    if Age==max(C):
        D+=Age
print(f'Idade do homem mais velho:{D}')
print('Média das idades:',A/2)
print(f'Novinhas:{B}')

