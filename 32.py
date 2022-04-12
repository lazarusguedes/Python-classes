Year = int(input('Ano:'))
if (Year % 4 == 0 and Year % 100 != 0) or Year % 400 == 0:
    print('Ano Bissexto')
else:
    print('Não é ano bissexto')