

import time
import random
import turtle
import tkinter
import math
import turtleBeads
from turtle import *
from turtleBeads import *
from tkinter import *


pen = turtle.Turtle()
wn = turtle.Screen()
wn.bgpic("felt.gif")
wn.setup(1200, 1000)
wn.title("Deck of Cards Simulator by ZimTKE")

#Used to generate symbol/text on bottom right of card
bottomright = turtle.getcanvas()


pen.speed(0)
pen.hideturtle()


#click to continue
# click = False
# def on_click(i, j):
	# global click
	# click = True

# turtle.onscreenclick(on_click)

# def waitforclick():
	# global click
	# turtle.update()
	# click = False
	# while not click:
		# turtle.update()
		# time.sleep(0.1)
		
	# click = False

# turtle.update()



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

	def render_opp(self, x, y, pen):
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
			

		#Draw suit in the middle
		if self.suit == "D" or self.suit == "H":
			pen.color("white")
			fill = "white"
		else:
			pen.color("white")
			fill = "white"
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

	def render_opp_lt(self, x, y, pen):
		#Draw border
		pen.penup()
		pen.goto(x, y)
		pen.color("black")
		pen.goto(x-76, y+51)
		pen.begin_fill()
		pen.pendown()
		pen.goto(x+76, y+51)
		pen.goto(x+76, y-51)
		pen.goto(x-76, y-51)
		pen.goto(x-76, y+51)
		pen.end_fill()
		pen.penup()
		pen.goto(x, y)
		pen.color("white")
		pen.goto(x-75, y+50)
		pen.begin_fill()
		pen.pendown()
		pen.goto(x+75, y+50)
		pen.goto(x+75, y-50)
		pen.goto(x-75, y-50)
		pen.goto(x-75, y+50)
		pen.end_fill()
		pen.penup()
			

		#Draw suit in the middle
		if self.suit == "D" or self.suit == "H":
			pen.color("white")
			fill = "white"
		else:
			pen.color("white")
			fill = "white"
		#pen.color("white")
		ctrsuit = bottomright.create_text(x, -y, text=self.symbols[self.suit], angle=270, font=("Courier New", 48, "normal"),fill=fill)
		
		#Draw top left
		toplttxt = bottomright.create_text(x-62, -y+35, text=self.name, angle=90, font=("Courier New", 16, "normal"), fill=fill)
		topltsuit = bottomright.create_text(x-45, -y+35, text=self.symbols[self.suit], angle=90, font=("Courier New", 16, "normal"),fill=fill)
		
		#Draw bottom right
		botrttxt = bottomright.create_text(x+62, -y-35, text=self.name, angle=270, font=("Courier New", 16, "normal"), fill=fill)
		botrtsuit = bottomright.create_text(x+45, -y-35, text=self.symbols[self.suit], angle=270, font=("Courier New", 16, "normal"),fill=fill)
	
	def render_opp_rt(self, x, y, pen):
		#Draw border
		pen.penup()
		pen.goto(x, y)
		pen.color("black")
		pen.goto(x-76, y+51)
		pen.begin_fill()
		pen.pendown()
		pen.goto(x+76, y+51)
		pen.goto(x+76, y-51)
		pen.goto(x-76, y-51)
		pen.goto(x-76, y+51)
		pen.end_fill()
		pen.penup()
		pen.goto(x, y)
		pen.color("white")
		pen.goto(x-75, y+50)
		pen.begin_fill()
		pen.pendown()
		pen.goto(x+75, y+50)
		pen.goto(x+75, y-50)
		pen.goto(x-75, y-50)
		pen.goto(x-75, y+50)
		pen.end_fill()
		pen.penup()
			

		#Draw suit in the middle
		if self.suit == "D" or self.suit == "H":
			pen.color("white")
			fill = "white"
		else:
			pen.color("white")
			fill = "white"
		#pen.color("white")
		ctrsuit = bottomright.create_text(x, -y, text=self.symbols[self.suit], angle=90, font=("Courier New", 48, "normal"),fill=fill)
		
		#Draw top left
		toplttxt = bottomright.create_text(x-62, -y+35, text=self.name, angle=90, font=("Courier New", 16, "normal"), fill=fill)
		topltsuit = bottomright.create_text(x-45, -y+35, text=self.symbols[self.suit], angle=90, font=("Courier New", 16, "normal"),fill=fill)
		
		#Draw bottom right
		botrttxt = bottomright.create_text(x+62, -y-35, text=self.name, angle=270, font=("Courier New", 16, "normal"), fill=fill)
		botrtsuit = bottomright.create_text(x+45, -y-35, text=self.symbols[self.suit], angle=270, font=("Courier New", 16, "normal"),fill=fill)
		
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

round = 7
#my cards
for i in range(round):
	#my cards
	card = deck.drawcard()
	card.render(i*85-260,-250, pen)

	#opponent to the left
	card = deck.drawcard()
	card.render_opp_lt(-450,-i*85+310, pen)

	#opponent accross from me	
	card = deck.drawcard()
	card.render_opp(-i*85+240,350, pen)

	#opponent to the right
	card = deck.drawcard()
	card.render_opp_rt(450,i*85-200, pen)



#making a button
CURSOR_SIZE = 20
FONT_SIZE = 12
FONT = ('Arial', FONT_SIZE, 'bold')

card = Card("", "")
card.render(-510,-400, pen)

def draw_onclick(x, y):
    card = deck.drawcard()
    card.render(-510,-400, pen)

#pen = Turtle()
pen.hideturtle()
pen.color("black")
pen.shape('circle')
pen.fillcolor('black')
pen.penup()
pen.goto(-510, -300)
pen.write("Click for Trump Card", align='center', font=FONT)
pen.sety(-340+ CURSOR_SIZE + FONT_SIZE)
pen.onclick(draw_onclick)
pen.showturtle()

pen = Turtle()
pen.hideturtle()


screen = Screen()
screen.mainloop()






wn.mainloop()
