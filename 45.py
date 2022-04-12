from random import choice
T = ['Rock','Paper','Scissors']
print('Rock, Paper, Scissors!')
C = input('Make your choice:')
R = choice(T)
print(f'Skynet: {R}')
if C == 'Rock':
    if R == 'Rock':
        print('Tie')
    elif R == 'Paper':
        print('Loser')
    elif R == 'Scissors':
        print('Winner')
if C == 'Paper':
    if R == 'Rock':
        print('Winner')
    elif R == 'Paper':
        print('Tie')
    elif R == 'Scissors':
        print('Loser')
if C == 'Scissors':
    if R == 'Rock':
        print('Loser')
    elif R == 'Paper':
        print('Winner')
    elif R == "Scissors":
        print('Tie')
