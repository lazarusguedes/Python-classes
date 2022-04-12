I = int(input('Cateto A:'))
II = int(input('Cateto B:'))
III = int(input('Hipotenusa:'))
if (I-II<III<I+II and II-III<I<II+III and I-III<II<I+III):
    print('Podem formar um triângulo')
else:
    print('Não podem formar uma triângulo')