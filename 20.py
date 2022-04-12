from random import sample, choice
I = (input('I:'))
II = (input('II:'))
III = (input('III:'))
IV = (input('IV:'))
x = [I,II,III,IV]
y = sample(x,k=4)
print(f'Students:{y}')