import random

class Card(object):
	def __init__(self, suit, val):
		self.suit = suit
		self.value = val
		
	def show(self):
		print("{} of {}".format(self.value, self.suit))
	
class Deck(object):
	def __init__(self):
		self.cards = []
		self.build()
	
	def build(self):
		for s in ["Spades", "Clubs", "Diamonds", "Hearts"]:
			for v in range(1, 14):
				self.cards.append(Card(s, v))
	
	def show(self):
		for c in self.cards:
			c.show()
	
	def shuffle(self):
		for i in range(len(self.cards)-1, 0, -1):
			r = random.randint(0, i)
			self.cards[i], self.cards[r] = self.cards[r], self.cards[i]
	
	def drawCard(self):
		return self.cards.pop()
		
	def flipCard(self):
		return self.cards.pop()
	
class Player(object):
	def __init__(self, name):
		self.name = name
		self.hand = []
	
	def draw(self, deck):
		self.hand.append(deck.drawCard())
		
	def flipCard(self, deck):
		self.hand.append(deck.flipCard())
	
	def showHand(self):
		for card in self.hand:
			card.show()
	
	def discard(self):
		return self.hand.pop()


deck = Deck()
deck.shuffle()
#deck.show()

bob = Player("Bob")
print(bob.name)
for i in range(0,7):
	bob.draw(deck)
bob.showHand()

mark = Player("Mark")
print(mark.name)
for i in range(0,7):
	mark.draw(deck)
mark.showHand()

bill = Player("Bill")
print(bill.name)
for i in range(0,7):
	bill.draw(deck)
bill.showHand()

mike = Player("Mike")
print(mike.name)
for i in range(0,7):
	mike.draw(deck)
mike.showHand()

dealer = Player("Dealer")
print(dealer.name)
dealer.flipCard(deck)
dealer.showHand()

