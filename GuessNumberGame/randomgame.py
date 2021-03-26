from random import randint
import sys

answer = randint(int(sys.argv[1]), int(sys.argv[2]))

for x1 in {int(sys.argv[1])}:
    num1 = x1

for x2 in {int(sys.argv[2])}:
    num2 = x2

while True:
    try:
        guess = input(
            f'Guess a number {int(sys.argv[1])}-{int(sys.argv[2])}: ')
        if num1-1 < int(guess) < num2+1:
            if int(guess) == answer:
                print('You are awsome!')
                break
        else:
            print(f'> {num1-1} and < {num2+1}')
    except ValueError:
        print('Please enter a number')
        continue
