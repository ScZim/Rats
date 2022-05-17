

import time
import random
import turtle
import tkinter
import math


wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(1200, 1000)
wn.title("Deck of Cards Simulator by ZimTKE")

pen = turtle.Turtle()
pen.speed(0)
pen.hideturtle()

#Used to generate symbol/text on bottom right of card
bottomright = turtle.getcanvas()

click = False
def on_click(i, j):
	global click
	click = True

turtle.onscreenclick(on_click)

def waitforclick():
	global click
	turtle.update()
	click = False
	while not click:
		turtle.update()
		time.sleep(0.1)
		
	click = False

turtle.update()



class Card(object):
	def __init__(self, name, suit):
		self.name = name
		self.suit = suit
		self.symbols = {"D":"♦", "C":"♣", "H":"♥", "S":"♠"}
	
	def print_card(self):
		
		print(f"{self.name}{self.symbols[self.suit]}")

#	def render(self, x, y, pen):
		#Draw border edge
#		pen.penup()
#		pen.goto(x, y)
#		pen.color("black")
#		pen.goto(x-52, y+77)
#		pen.begin_fill()
#		pen.pendown()
#		pen.goto(x+52, y+77)
#		pen.goto(x+52, y-77)
#		pen.goto(x-52, y-77)
#		pen.goto(x-52, y+77)
#		pen.end_fill()
#		pen.penup()
		
	def render(self, x, y, pen):
		#Draw border
		pen.penup()
		pen.goto(x, y)
		pen.color("black")
		pen.goto(x-51, y+76)
		pen.begin_fill()
		pen.pendown()
		pen.goto(x+51, y+76)
		pen.goto(x+51, y-76)
		pen.goto(x-51, y-76)
		pen.goto(x-51, y+76)
		pen.end_fill()
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
			
		if self.name != "":
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

#my cards
for i in range(7):
	card = deck.drawcard()
	card.render(i*85-250,-250, pen)

#opponent to the left
for i in range(7):
	card = Card("", "")
	card.render(-450,i*65-150, pen)

waitforclick()
	
for i in range(7):
	card = deck.drawcard()
	card.render(-450,i*65-150, pen)

#opponent accross from me	
for i in range(7):
	card = Card("", "")
	card.render(i*85-250,350, pen)

waitforclick()

for i in range(7):
	card = deck.drawcard()
	card.render(i*85-250,350, pen)

#opponent to the right
for i in range(7):
	card = Card("","")
	card.render(450,i*65-150, pen)

waitforclick()

for i in range(7):
	card = deck.drawcard()
	card.render(450,i*65-150, pen)

	
#card = deck.drawcard()
#card.render(0,0, pen)





wn.mainloop()
