import random as rnd
import time

class Dice():
	n = None
	
	def rollDice(self):
		self.n = rnd.randint(1, 6)
		return self.n
		
p1 = Dice()
p2 = Dice()

def game(player1, player2, n):
	win1 = []
	win2 = []
	
	for i in range(n):
		time.sleep(2)
		
		x = p1.rollDice()
		y = p2.rollDice()
		
		print("[{0}: {a} - {b} :{1}]".format(player1, player2, a = str(x), b = str(y)))
		
		if x > y:
			print(player1 + " wins!\n")
			win1.append(1)
		elif y > x:
			print(player2 + " wins!\n")
			win2.append(2)
		elif x == y:
			print("It's a draw!\n")
			
	if len(win1) > len(win2):
		print("\n {0} wins the best of {1}".format(player1, n))
	elif len(win2) > len(win1):
		print("\n {0} wins the best of {1}".format(player2, n))
	elif len(win1) == len(win2):
		print("\nnobody wins\n")
		n -= 2
		if n < 0:
			n = 3
		game(player1, player2, n)
		
#let's check it out
game("Fr4nkl1n", "Harrixcode", 5)

#Please rate!
