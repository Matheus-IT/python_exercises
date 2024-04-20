from random import randint


DRAWN_NUMBER = randint(1, 101)
print('Cheat:', DRAWN_NUMBER)

MAXIMUM_ATTEMPTS = 5

tip = ''
plays = 0

while True:
	print(tip)
	guess = int(input('Guess a number: '))

	if guess < DRAWN_NUMBER:
		tip = 'Tip: the number is greater than your last guess...'
	elif guess > DRAWN_NUMBER:
		tip = 'Tip: the number is smaller than your last guess...'
	else:
		print('You nailed it! Congratulations!!😃')
		break

	plays += 1

	print(f'You have {MAXIMUM_ATTEMPTS - plays} guesses left...')

	if plays == MAXIMUM_ATTEMPTS:
		print('I\'m sorry, you ran out of guesses... 😟')
		break

print('Game over')
