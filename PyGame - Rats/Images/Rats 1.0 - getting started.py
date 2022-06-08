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

font_main = pg.font.SysFont(None, 75)
font_sub = pg.font.SysFont(None, 50)
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
		
		playercard = pg.image.load(f"{self.name}{self.suit}.png")
		playercardsm = pg.transform.scale(playercard, (150, 210))
		screen.blit(playercardsm, (500+50, 750 ))

			
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
		
	def flipCard(self, deck):
		self.hand.append(deck.flipCard())
	
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

bob = Player("Bob")
#print(bob.name)

bob.draw(deck)
bob.showHand()
bob.draw(deck)
bob.showHand()

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
		draw_text('Main Menu', font_main, (255, 255, 255), screen, 550, 150)
		
		mx, my = pg.mouse.get_pos()
		
		button_1 = pg.Rect(580, 250, 200, 50)
		
		button_2 = pg.Rect(580, 350, 200, 50)
		
		
		if button_1.collidepoint((mx, my)):
			if click:
				game()
		if button_2.collidepoint((mx, my)):
			if click:
				rules()
		pg.draw.rect(screen, (0, 0, 0), button_1)
		pg.draw.rect(screen, (0, 0, 0), button_2)
		draw_text('Play Game', font_sub, (100, 100, 100), screen, 590, 259)
		draw_text('Rules', font_sub, (100, 100, 100), screen, 635, 359)
		click = False
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
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
		for card in bob.hand:
			bob.showcard()
		
	
		#Input events
		for event in pg.event.get():
			if event.type == pg.QUIT:
				gameLoop = False
			if event.type == pg.KEYDOWN:
				gameLoop = False

		pg.display.update()

	
def rules():
	rules = True
	while rules:
		#Load background image
		screen.blit(bgImage, bgImageRect)
		
		#Move Card to the left
#		dealtcardX -= 5
		#Load Card
		cardstack()
		dealtcard(dealtcardX, dealtcardY)
	
		#show bobs cards
		for card in bob.hand:
			bob.showcard()
		
	
		#Input events
		for event in pg.event.get():
			if event.type == pg.QUIT:
				rules = False
			if event.type == pg.KEYDOWN:
				rules = False

		pg.display.update()



main_menu()
