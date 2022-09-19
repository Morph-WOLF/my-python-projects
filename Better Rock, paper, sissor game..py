import itertools as it
ROCK = 0
PAPER = 1
SCISSOR = 2
PLAYER = 0
COMPUTER = 1
TIE = 2

winner = []
for i in range(3):
  winner.append([])
  for j in range(3):
    winner[i].append(0)

winner[ROCK][ROCK] = TIE
winner[ROCK][PAPER] = COMPUTER
winner[ROCK][SCISSOR] = PLAYER
winner[PAPER][ROCK] = PLAYER
winner[PAPER][PAPER] = TIE
winner[PAPER][SCISSOR] = COMPUTER
winner[SCISSOR][ROCK] = COMPUTER
winner[SCISSOR][PAPER] = PLAYER
winner[SCISSOR][SCISSOR] = TIE



