__author__ = 'vincentc'
number = 23
guess = int(input('enter an integer : '))
if guess == number:
    print('congratulations,you guessed it.')
    print('(but you don\'t win any prizes)')
elif guess < number:
    print('No,it is a little higher than that')
else:
    print('no,it is little lower than that')
print('done')