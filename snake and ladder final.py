"""
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
"""
import random
import time
player1=0
player2=0
def snakes_and_ladders(n):
    snakes={27:1,21:9,17:4,19:7}
    ladders={11:24,3:22,5:8,20:29}
    if n in ladders:
        print("Its a ladder climb up")
        n=ladders[n]
    elif n in snakes:
        print("Its a snake!!,Come down")
        n=snakes[n]
    return n
print("WELCOME TO SNAKES AND LADDERS GAME!!!")
def roll_dice(r):
    min=1
    max=6
    print("Rolling the dice......:)")
    t=(random.randint(min,max))
    print(t)
    if ((r==25 and t==6) or (r==26 and t>=5) or (r==27 and t>=4) or (r==28 and t>=3) or (r==29 and t>=2)):
        print("Oops!! you reach out of board. There wont be any improvement")
        
    else:
        r=r+t
        if t==6:
            print("Yayyy you get another chance")
            t=(random.randint(min,max))
            print(t)
            if ((r==25 and t==6) or (r==26 and t>=5) or (r==27 and t>=4) or (r==28 and t>=3) or (r==29 and t>=2) or r==30):
                print("Oops!! you reach out of board. There wont be any improvement")
                r=r-6
            else:
                r=r+t
        
    return r
    
        
    
while player1 <= 29 or player2 <= 29:
	print("Its turn of player1\n")
	time.sleep(2)
	player1 = roll_dice(player1)
	time.sleep(2)
	player1 = snakes_and_ladders(player1)
	time.sleep(2)
	print("Current status of Player1:",player1,"and Player2:",player2)
	time.sleep(2)

	if player1 == 30:
		print("Winner of the game is PLAYER1!!!")
		break
	    

	print("Its turn of player2\n")
	time.sleep(2)
	player2 = roll_dice(player2)
	time.sleep(2)
	player2 = snakes_and_ladders(player2)
	time.sleep(2)
	print("Current status of Player1:",player1," and Player2:",player2)
	time.sleep(2)

	if player2 == 30:
		print("Winner of the game is PLAYER2!!!")
		break
       
        
