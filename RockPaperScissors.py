from random import choice

hand = ['Rock', 'Paper', 'Scissors']

c = 0
p = 0

while True:
	computer = choice(hand)

	player = input(" Rock, Paper, or Scissors?! > ")

	# to end game
	if (player == 'n') or (player == 'no') or (player == 'bye') or (player == 'N') or (player == 'No') or (player == 'Bye'):
		print(' Bye... See you next time!')
		print(' ' + str(c) + ' : ' + str(p))
		break

	# for different options / abbreviations
	if (player == 'rock') or (player == 'r') or (player == 'R'):
		player = 'Rock'

	elif (player == 'paper') or (player == 'p') or (player == 'P'):
		player = 'Paper'

	elif (player == 'scissors') or (player == 's') or (player == 'S'):
		player = 'Scissors'

	# actaul comparison and display
	if computer == player:
		print(' We both chose ' + computer + '. So, it\'s a tie')
		print(' ' + str(c) + ' : ' + str(p))

	elif (computer == 'Rock') and (player == 'Paper'):
		print(' I chose Rock, you chose Paper. You won!')

		p = p + 1
		print(' ' + str(c) + ' : ' + str(p))

	elif (computer == 'Rock') and (player == 'Scissors'):
		print(' I chose Rock, you chose Scissors. I won!')

		c = c + 1
		print(' ' + str(c) + ' : ' + str(p))

	elif (computer == 'Paper') and (player == 'Scissors'):
		print(' I chose Paper, you chose Scissors. You won!')

		p = p + 1
		print(' ' + str(c) + ' : ' + str(p))

	elif (computer == 'Paper') and (player == 'Rock'):
		print(' I chose Paper, you chose Rock. I won!')

		c = c + 1
		print(' ' + str(c) + ' : ' + str(p))

	elif (computer == 'Scissors') and (player == 'Rock'):
		print(' I chose Scissors, you chose Rock. You won!')

		p = p + 1
		print(' ' + str(c) + ' : ' + str(p))

	elif (computer == 'Scissors') and (player == 'Paper'):
		print(' I chose Scissors, you chose Paper. I won!')

		c = c + 1
		print(' ' + str(c) + ' : ' + str(p))

	else:
		print(' Try Again!')
