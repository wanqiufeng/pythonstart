__author__ = 'vincentc'
number = 23
running = True

while running:
    guess = int(input('enter an integer : '))
    if guess == number:
        print('congratulations,you guessed it.')
        print('(but you don\'t win any prizes)')
        running = False
    elif guess < number:
        print('No,it is a little higher than that')
    else:
        print('no,it is little lower than that')
else:
    print('loop over')
print('done')