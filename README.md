# Snake-and-Ladder-game-in-Python

Objective:
Implementation of Snake and Ladder game in Python

Algorithm for Snakes and Ladders game in python
	1)There are two players and they are given a dice
	2)Typically the game board has 30 cells starting from 1 to 30
	3)There are snakes and ladders in different cells. And each has either a ladder or a snake or nothing but not both snake and ladder in the same cell.
	4)We use two python dictionaries namely 'snakes' and 'ladders' to declare the positions of snakes and ladders.
	5)We make starting cell number of snake or ladder as 'key' and ending cell number as 'value' of the dictionary.
	6)Define a function to roll the dice i.e., accepting the input from Player1 and Player2 with a checking condition of dice number to be between 1 & 6.
	7)Define a function to check if Player1 or Player2 found ladder or a snake mouth.
	8)Check for the 'key's in both dictionaries & proceed accordingly.
	9)The rolling of dice continues until any of the player reaches above 29, if any of the players reach 30 they will be declared as winner of the game.
