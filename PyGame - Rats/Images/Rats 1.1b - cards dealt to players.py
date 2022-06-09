import pygame
import random
import math
import pygame as pg
import time
from pygame import *
mainClock = pg.time.Clock()
pg.init()

#Load the pygame screen
screen = pg.display.set_mode((1400, 1000))
pg.display.set_caption("RATS - A ZimTKE Production")
gameIcon = pg.image.load('ratimage.png')
pg.display.set_icon(gameIcon)

#Load Background image into Python
bgImage = pg.image.load('felt.gif')
bgImageRect = bgImage.get_rect()

#Cards
cardImg = pg.image.load('gray_back.png')
cardsmall = pg.transform.scale(cardImg, (150, 210))

cardstackX = 1200
cardstackY = 750

dealtcardX = 1200
dealtcardY = 750

font_main = pg.font.SysFont('gadugi', 85)
font_sub = pg.font.SysFont(None, 50)
font_tiny = pg.font.SysFont('gadugi', 14)
#Create Cards
class Card(object):
	def __init__(self, name, suit):
		self.name = name
		self.suit = suit
#		self.symbols = {"D":"♦", "C":"♣", "H":"♥", "S":"♠"}
	
	#print hands in terminal
	def show(self):
		print(f"{self.name}{self.suit}")
	
	#render the cards that are in our hand, gotta work on these positions
	def render(self):
		
		for x,card in enumerate(me.hand):
			playercard = pg.image.load(f"{card.name}{card.suit}.png")
			playercardsm = pg.transform.scale(playercard, (150, 210))
			screen.blit(playercardsm, (450+50*x, 750))
		
		for x,card in enumerate(p1.hand):
			playercard = pg.image.load(f"{card.name}{card.suit}.png")
			playercardsm = pg.transform.scale(playercard, (150, 210))
			screen.blit(playercardsm, (50, 200+50*x))
		
		for x,card in enumerate(p2.hand):
			playercard = pg.image.load(f"{card.name}{card.suit}.png")
			playercardsm = pg.transform.scale(playercard, (150, 210))
			screen.blit(playercardsm, (450+50*x, 25))
		
		for x,card in enumerate(p3.hand):
			playercard = pg.image.load(f"{card.name}{card.suit}.png")
			playercardsm = pg.transform.scale(playercard, (150, 210))
			screen.blit(playercardsm, (1200, 200+50*x))

			
#Create Deck
class Deck():
	def __init__(self):
		self.cards = []
		names = ("A", "K", "Q", "J", "10", "9", "8", "7", "6", "5", "4", "3", "2")
		suits = ("D", "H", "S", "C")
		
		for name in names:
			for suit in suits:
				card = Card(name, suit)
				self.cards.append(card)
				
	def show(self):
		for c in self.cards:
			c.show()
	
	def shuffle(self):
		random.shuffle(self.cards)

	def drawCard(self):
		card = self.cards.pop()
		return card

#Create Player		
class Player(object):
	def __init__(self, name):
		self.name = name
		self.hand = []
	
	def draw(self, deck):
		self.hand.append(deck.drawCard())

	def showHand(self):
		for card in self.hand:
			card.show()
			
	def showcard(self):		
		for card in self.hand:
			card.render()
	
	def discard(self):
		return self.hand.pop()


#Create deck
deck = Deck()
#Shuffle deck
deck.shuffle()

me = Player("Me")
p1 = Player("Player 1")
p2 = Player("Player 2")
p3 = Player("Player 3")
#print(bob.name)

roundnum = 1

for _ in range(8-roundnum):
	me.draw(deck)
	p1.draw(deck)
	p2.draw(deck)
	p3.draw(deck)
me.showHand()
#bob.draw(deck)
#bob.showHand()

def cardstack():
	for i in range(12):
		screen.blit(cardsmall, (cardstackX + i/1.25, cardstackY + i/1.5))

def dealtcard(x, y):
	screen.blit(cardsmall, (dealtcardX + 12/1.25, dealtcardY + 12/1.5))

def draw_text(text, font, color, surface, x, y):
	textobj = font.render(text, 1, color)
	textrect = textobj.get_rect()
	textrect.topleft = (x, y)
	surface.blit(textobj, textrect)

click = False
#Create Main Menu
def main_menu():
	while True:
		
		screen.blit(bgImage, bgImageRect)
		draw_text('Main Menu', font_main, (255, 255, 255), screen, 485, 120)
		
		mx, my = pg.mouse.get_pos()
		
		button_1 = pg.Rect(600, 250, 200, 50)
		
		button_2 = pg.Rect(600, 325, 200, 50)
		
		
		if button_1.collidepoint((mx, my)):
			if click:
				game()
		if button_2.collidepoint((mx, my)):
			if click:
				rules()
		pg.draw.rect(screen, (0, 0, 0), button_1)
		pg.draw.rect(screen, (0, 0, 0), button_2)
		draw_text('Play Game', font_sub, (100, 100, 100), screen, 610, 259)
		draw_text('Rules', font_sub, (100, 100, 100), screen, 655, 334)
		click = False
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				
			if event.type == pg.KEYDOWN:
				if event.key == K_ESCAPE:
					pg.quit()
			if event.type == pg.MOUSEBUTTONDOWN:
				if event.button == 1:
					click = True
		
		pg.display.update()
		mainClock.tick(60)	

def game():
	gameLoop = True
	while gameLoop:
		#Load background image
		screen.blit(bgImage, bgImageRect)
		
		#Move Card to the left
	#	dealtcardX -= 5
		#Load Card
		cardstack()
		dealtcard(dealtcardX, dealtcardY)
	
		#show bobs cards
		me.showcard()
		p1.showcard()
		p2.showcard()
		p3.showcard()
	
		#Input events
		for event in pg.event.get():
			if event.type == pg.QUIT:
				gameLoop = False
			if event.type == pg.KEYDOWN:
				gameLoop = False

		pg.display.update()

#Rules Page
RuleImg = pg.image.load('2Dblank.png')
RuleImgSmall = pg.transform.scale(RuleImg, (450, 630))
	
def rules():
	rules = True
	while rules:
		#Load background image
		screen.blit(bgImage, bgImageRect)
		screen.blit(RuleImgSmall, (476,200))
		draw_text('RULES', font_main, (0, 0, 0), screen, 590, 195)
		draw_text('RATS is a multi-round game.', font_tiny, (0, 0, 0), screen, 550, 315)
		draw_text('In the first round, each player is dealt 7 cards.', font_tiny, (0, 0, 0), screen, 550, 335)
		draw_text('One card from the remaining deck is flipped face', font_tiny, (0, 0, 0), screen, 550, 355)
		draw_text('     up, determining the trump (best) suit.', font_tiny, (0, 0, 0), screen, 550, 370)
		draw_text('The player left of the dealer plays the first card.', font_tiny, (0, 0, 0), screen, 550, 390)
		draw_text('The rest of the players must follow suit if they', font_tiny, (0, 0, 0), screen, 550, 410)
		draw_text('     can.', font_tiny, (0, 0, 0), screen, 550, 425)
		draw_text('The person that plays the highest card (Aces are', font_tiny, (0, 0, 0), screen, 550, 445)
		draw_text('     high) takes the trick.', font_tiny, (0, 0, 0), screen, 550, 460)
		draw_text('If a player cannot follow suit, they may play a', font_tiny, (0, 0, 0), screen, 550, 480)
		draw_text('     trump card.', font_tiny, (0, 0, 0), screen, 550, 495)
		draw_text('If a player plays a trump card, the highest', font_tiny, (0, 0, 0), screen, 550, 515)
		draw_text('     trump card takes the trick.', font_tiny, (0, 0, 0), screen, 550, 530)
		draw_text('All players that take at least one trick', font_tiny, (0, 0, 0), screen, 550, 550)
		draw_text('     advance to the next round.', font_tiny, (0, 0, 0), screen, 550, 565)
		draw_text('The player that takes the most tricks in the previous', font_tiny, (0, 0, 0), screen, 550, 585)
		draw_text('     round gets to determine trump for the next round', font_tiny, (0, 0, 0), screen, 550, 600)
		draw_text('     after viewing their cards.', font_tiny, (0, 0, 0), screen, 550, 615)
		draw_text('A player may not LEAD trump until it has been', font_tiny, (0, 0, 0), screen, 550, 635)
		draw_text('     played or is the only remaining suit in hand', font_tiny, (0, 0, 0), screen, 550, 650)
		draw_text('Each round is played with one less card (7, 6, 5...)', font_tiny, (0, 0, 0), screen, 550, 670)
		draw_text('The game ends when a player takes all tricks in a', font_tiny, (0, 0, 0), screen, 550, 690)
		draw_text('     round. No matter the round.', font_tiny, (0, 0, 0), screen, 550, 705)
		draw_text('The 2 of Diamonds is the best card in the game.', font_tiny, (0, 0, 0), screen, 550, 725)
		draw_text('Optional - When a player does not get a single', font_tiny, (0, 0, 0), screen, 550, 745)
		draw_text('     trick, they are eliminated. They may now', font_tiny, (0, 0, 0), screen, 550, 760)
		draw_text('     shout RRRRRRRRATS..', font_tiny, (0, 0, 0), screen, 550, 775)
		
		
	
		#Input events
		for event in pg.event.get():
			if event.type == pg.QUIT:
				rules = False
			if event.type == pg.KEYDOWN:
				rules = False

		pg.display.update()



main_menu()
