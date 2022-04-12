I=(input('I:'))
II=(input('II:'))

print('I:')
print('Tipo:',type(I))
print('número e letra?',I.isalnum())
print('número?',I.isnumeric())
print('letra?',I.isalpha())
print('Decimal?',I.isdecimal())
print('dígito?',I.isdigit())

print('II:')
print(type(II))
print(II.isalnum())
print(II.isnumeric())
print(II.isalpha())
print(II.isdecimal())
print(II.isdigit())


OBS:
N = 'suckers'
print(f'So long, {N}!')