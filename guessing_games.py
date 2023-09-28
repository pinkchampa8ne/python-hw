# Write your code here :-)

import random

my_random_number = random.randint(1, 100)  # a random integer between 1 and 100, inclusive

def guessing_game(rand = my_random_number):
    answer = input("Guess the number I'm thinking of! It's between 1 and 100, inclusive.")
    if int(answer) > 100 or int(answer) < 1:
        raise ValueError('That is outside of the possible choices.')
    if int(answer) == rand:
        print('Correct! You win!')
    if int(answer) > rand:
        print('Too high!')
        guessing_game()
    if int(answer) < rand:
        print('Too low!')
        guessing_game()

#guessing_game()

def guessing_game1():
    print('Think of a number between 1 and 100, inclusive, and I will try to guess it.')
    print('If I am correct, type "y".')
    print('If I am too high, type "h".')
    print('If I am too low, type "l".')
    loop()

def loop(my_guess = random.randint(1,100), maximum = 100, minimum = 1):
    if maximum - minimum == 0:
        my_guess = maximum
        print('Your number must be', maximum, '!')
    else:
        print('Is it', my_guess, '?')
        response = input('Answer here:')
        if response == 'y':
            print('I got it!')
        if response == 'h':
            if my_guess == minimum:
                raise ValueError('That is the minimum value.')
            else:
                maximum = my_guess - 1
                my_guess = random.randint(minimum,maximum)
                loop(my_guess, maximum, minimum)
        if response == 'l':
            if my_guess == maximum:
                raise ValueError('That is the maximum value.')
            else:
                minimum = my_guess + 1
                my_guess = random.randint(minimum,maximum)
                loop(my_guess, maximum, minimum)
        if response != 'y' and response != 'h' and response != 'l':
            raise ValueError('Please enter a valid response.')

guessing_game1()
