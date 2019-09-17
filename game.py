from tkinter import *
from PIL import ImageTk,Image
import random
import time

suits = ['S', 'D', 'C', 'H']


class card():

	def __init__(self, root, suit, value):
		self.suit = suits[suit]
		self.value = value
		self.root = root
		#self.gui()

	def gui(self):

		def getImage():
			image = Image.open('Assets/{}{}.png'.format(self.value, self.suit[0]))
			image = image.resize((150,230), Image.ANTIALIAS)
			global img
			img = ImageTk.PhotoImage(image)
			self.cardCanvas.create_image(5, 5, image=img, anchor=NW)

		self.cardCanvas = Canvas(self.root, width = 155, height = 235)
		self.cardCanvas.bind("<button1>", self.selected())
		self.cardCanvas.grid(row=0, column=1)

		getImage()

	def changeState(self):
		self.cardCanvas

	def selected(self):
		if self.cardCanvas['background'] == 'blue':
			self.cardCanvas.configure(bg ='white')
		else:
			self.cardCanvas.configure(bg='blue')

	def getValue(self):
		return self.value

	def getSuit(self):
		return self.suit


class gameController():

	def __init__(self, numberOfPlayers: str, startingMoney: int, root: object):
		self.root = root
		self.players = []
		for p in range(numberOfPlayers):
			self.players.append([numberOfPlayers, startingMoney])
		self.generateCards()


	def generateCards(self):
		self.deck = []
		for suit in range(4):
			for value in range(1,14):
				s = suits[suit]
				c = card(self.root, s, value)
				self.deck.append(c)

	def shuffle(self):
		tempPack = []
		for x in range(52):
			cardPosition = random.randint(0, len(self.deck) - 1)
			tempPack.append(self.deck.pop(cardPosition))
		self.deck = tempPack

	def getDeck(self):
		return self.deck


	def deal(self):
		pass

def handRating(playerCards, riverCards):
	totalHand = []
	for c in playerCards:
		val  = c.getValue()
		suit = c.getSuit()
		totalHand.append([val, suit])
	for c in riverCards:
		val = c.getValue()
		suit = c.getSuit()
		totalHand.append([val, suit])

	count_array = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for x in totalHand:
		count[x[0] - 1] += 1

	def flush():
		suitCount = [0,0,0,0]
		for x in totalHand:
			if x[1] == 'S':
				suitCount[0] += 1
			elif x[1] == 'D':
				suitCount[1] += 1
			elif x[1] == 'C':
				suitCount[2] += 1
			elif x[1] == 'H':
				suitCount[3] += 1
		if 5 in suitCount or 6 in suitCount or 7 in suitCount:
			return True
		else:
			return False

	def straight():
		totalHand.sort()
		numberOnly = []
		for x in totalHand:
			if not x[0] in numberOnly: #removes duplicates as this doesn't affect straights
				numberOnly.append(x[0])
			if 14 in numberOnly:
				numberOnly.append(1) #this means ace can be used for a low or high run
		run = 0
		for x in range(len(numberOnly) - 1):
			if numberOnly[x] + 1== numberOnly[x+1]:
				run += 1
			else:
				run = 0
			if run == 5:
				return True

		return False

	def four_of_a_kind():
		if 4 in count_array:
			return True
		else:
			return False

	def full_house():
		if 3 in count_array and 2 in count_array:
			return True
		else:
			return False

	def three_of_a_kind():
		if 3 in count_array:
			return True
		else:
			return False

	def two_pairs():
		if 2 in count_array:
			temp = count_array
			temp.remove(2) #remove first 2
			if 2 in temp:
				return True
			else:
				return False
		else:
			return False

	def pair():
		if 2 in count_array:
			return True
		else:
			return False

	def score_definer():
		score = 0
		if flush() and straight():
			score +=




def main():
	deck = []
	for s in range(4):
		for x in range(1, 15):
			c = card('root', s, x)
			deck.append(c)
	river = []
	player = []
	while len(river) < 5:
		num = random.randint(0, len(deck) - 1)
		selectedCard = deck[num]
		if not selectedCard in river:
			river.append(selectedCard)
	while len(player) < 2:
		num = random.randint(0, len(deck) - 1)
		selectedCard = deck[num]
		if not selectedCard in river or player:
			player.append(selectedCard)


	handRating(player, river)








if __name__ == '__main__':
	#game = gameController(3, 10000, 'a')
	#root = Tk()
	#root.geometry('600x600')
	main()

	#root.mainloop()
