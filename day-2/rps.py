import os

path = os.path.dirname(os.path.realpath(__file__))
file = os.path.join(path, 'input.txt')

player1_wins = 0
player2_wins = 0
wrong = 0

with open(file, 'r') as f:
	for line in f:
		p1Choice, p2Choice = line.split(' ')

		# Player 1: Rock A, Paper B, Scissors C
		# Player 2: Rock X, Paper Y, Scissors Z

		# Convert choices to strings
		p1Choice = str(p1Choice)
		p2Choice = str(p2Choice).split('\n')[0]

		print('Player 1:')
		print(p1Choice)
		print('Player 2:')
		print(p2Choice)
		print('')

		# If Rock is chosen add 1 to the score
		if p1Choice == 'A':
			player1_wins += 1
			print('Added 1 to Player 1 for Rock')
		if p2Choice == 'X':
			player2_wins += 1
			print('Added 1 to Player 2 for Rock')

		# If Paper is chosen add 2 to the score
		if p1Choice == 'B':
			player1_wins += 2
			print('Added 2 to Player 1 for Paper')
		if p2Choice == 'Y':
			player2_wins += 2
			print('Added 2 to Player 2 for Paper')

		# If Scissors is chosen add 3 to the score
		if p1Choice == 'C':
			player1_wins += 3
			print('Added 3 to Player 1 for Scissors')
		if p2Choice == 'Z':
			player2_wins += 3
			print('Added 3 to Player 2 for Scissors')
		
		if p1Choice == 'A' and p2Choice == 'Z':
			player1_wins += 6
			player2_wins += 0
			print('Added 6 to Player 1 for Rock beats Scissors')
		elif p1Choice == 'B' and p2Choice == 'X':
			player1_wins += 6
			player2_wins += 0
			print('Added 6 to Player 1 for Paper beats Rock')
		elif p1Choice == 'C' and p2Choice == 'Y':
			player1_wins += 6
			player2_wins += 0
			print('Added 6 to Player 1 for Scissors beats Paper')

		elif p1Choice == 'A' and p2Choice == 'Y':
			player1_wins += 0
			player2_wins += 6
			print('Added 6 to Player 2 for Paper beats Rock')
		elif p1Choice == 'B' and p2Choice == 'Z':
			player1_wins += 0
			player2_wins += 6
			print('Added 6 to Player 2 for Scissors beats Paper')
		elif p1Choice == 'C' and p2Choice == 'X':
			player1_wins += 0
			player2_wins += 6
			print('Added 6 to Player 2 for Rock beats Scissors')

		elif p1Choice == 'A' and p2Choice == 'X':
			player1_wins += 3
			player2_wins += 3
			print('Add 3 to both players for Rock ties Rock')
		elif p1Choice == 'B' and p2Choice == 'Y':
			player1_wins += 3
			player2_wins += 3
			print('Add 3 to both players for Paper ties Paper')
		elif p1Choice == 'C' and p2Choice == 'Z':
			player1_wins += 3
			player2_wins += 3
			print('Add 3 to both players for Scissors ties Scissors')

		else: 
			print('No winner')
			print('Something went wrong')
			wrong += 1
			print('')
				

print('Total Player Scores:')
print('Player 1: ' + str(player1_wins))
print('Player 2: ' + str(player2_wins))
print('Wrong: ' + str(wrong))
print('')
