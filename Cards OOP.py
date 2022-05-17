

import time
import random
import turtle
import tkinter
import math


wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(800, 600)
wn.title("Deck of Cards Simulator by ZimTKE")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

bottomright = turtle.getcanvas()




class Card(object):
	def __init__(self, name, suit):
		self.name = name
		self.suit = suit
		self.symbols = {"D":"♦", "C":"♣", "H":"♥", "S":"♠"}
	
	def print_card(self):
		
		print(f"{self.name}{self.symbols[self.suit]}")
		
	def render(self, x, y, pen):
		#Draw border
		pen.penup()
		pen.goto(x, y)
		pen.color("white")
		pen.goto(x-50, y+75)
		pen.begin_fill()
		pen.pendown()
		pen.goto(x+50, y+75)
		pen.goto(x+50, y-75)
		pen.goto(x-50, y-75)
		pen.goto(x-50, y+75)
		pen.end_fill()
		pen.penup()
		
		#Draw suit in the middle
		if self.suit == "D" or self.suit == "H":
			pen.color("red")
			fill = "red"
		else:
			pen.color("black")
			fill = "black"
		#pen.color("white")
		pen.goto(x-16, y-37)
		pen.write(self.symbols[self.suit], False, font=("Courier New", 48, "normal"))
		
		#Draw top left
		pen.goto(x-40, y+48)
		pen.write(self.name, False, font=("Courier New", 16, "normal"))
		pen.goto(x-40, y+31)
		pen.write(self.symbols[self.suit], False, font=("Courier New", 16, "normal"))
		
		#Draw bottom right
		botrttxt = bottomright.create_text(x+35, -y+62, text=self.name, angle=180, font=("Courier New", 16, "normal"), fill=fill)
		botrtsuit = bottomright.create_text(x+35, -y+45, text=self.symbols[self.suit], angle=180, font=("Courier New", 16, "normal"),fill=fill)
		
		#This draws the name and symbol right side up instead of upside down
		#pen.goto(x+35, y-75)
		#pen.write(self.name, False, font=("Courier New", 16, "normal"))
		#pen.goto(x+35, y-63)
		#pen.write(self.symbols[self.suit], False, font=("Courier New", 16, "normal"))
		
class Deck():
	def __init__(self):
		self.cards = []
		names = ("A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2")
		suits = ("D", "H", "S", "C")
		
		for name in names:
			for suit in suits:
				card = Card(name, suit)
				self.cards.append(card)
	
	def shuffle(self):
		random.shuffle(self.cards)

	def drawcard(self):
		card = self.cards.pop()
		return card

#Create deck
deck = Deck()
#Shuffle deck
deck.shuffle()

#render 7 cards, last 2 lines of code dont work with botrttxt/suit
for i in range(7):
	card = deck.drawcard()
	card.render(i*110-350, i*35, pen)
#	time.sleep(5)
#	pen.clear()


	
#card = deck.drawcard()
#card.render(0,0, pen)





wn.mainloop()
