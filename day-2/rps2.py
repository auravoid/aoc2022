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
		#  X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win.

		# Convert choices to strings
		p1Choice = str(p1Choice)
		p2Choice = str(p2Choice).split('\n')[0]

		print('Player 1:')
		print(p1Choice)
		print('Player 2:')
		print(p2Choice)

		if p2Choice == 'X':
			print('Lose')
			print('')
			if p1Choice == 'A':
				player1_wins += 1
				player2_wins += 3
			elif p1Choice == 'B':
				player1_wins += 2
				player2_wins += 1
			elif p1Choice == 'C':
				player1_wins += 3
				player2_wins += 2
			player1_wins += 6
			player2_wins += 0
			
		elif p2Choice == 'Y':
			print('Tie')
			print('')
			if p1Choice == 'A':
				player1_wins += 1
				player2_wins += 1
			elif p1Choice == 'B':
				player1_wins += 2
				player2_wins += 2
			elif p1Choice == 'C':
				player1_wins += 3
				player2_wins += 3
			player1_wins += 3
			player2_wins += 3

		elif p2Choice == 'Z':
			print('Win')
			print('')
			if p1Choice == 'A':
				player1_wins += 1
				player2_wins += 2
			elif p1Choice == 'B':
				player1_wins += 2
				player2_wins += 3
			elif p1Choice == 'C':
				player1_wins += 3
				player2_wins += 1
			player1_wins += 0
			player2_wins += 6

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
