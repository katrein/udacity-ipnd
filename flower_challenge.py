# Lesson 3.3: Use Classes
# Mini-Project: Epic Flower Challenge

import turtle
import webbrowser
import time

window = turtle.Screen()
window.bgcolor("black")

def epic_music():
	webbrowser.open("https://www.youtube.com/watch?v=eYj8ciqAPcA")

def draw_petals():
	petal = turtle.Turtle()
	petal.shape("circle")
	petal.color("#FF4C65")
	petal.pensize(2)
	petal.speed(1)
	
	i = 0
	while i < 36:
		petal.left(45)
		petal.forward(100)
		petal.left(135)
		petal.left(10)
		petal.forward(100)
		i += 1
	petal.penup()
	petal.left(10)

def draw_stem():
	stem = turtle.Turtle()
	stem.shape("turtle")
	stem.color("#007034")
	stem.pensize(5)
	stem.speed(1)
	
# re-positioning turtle for drawing stem:
	stem.penup()
	stem.right(180)
	stem.forward(10)
	stem.left(90)
	stem.forward(60)
	stem.pendown()

# drawing stem:
	stem.forward(60)

# drawing first leaf:
	stem.left(135)
	stem.forward(50)
	stem.right(45)
	stem.forward(50)
	stem.right(135)
	stem.forward(50)
	stem.right(45)
	stem.forward(50)

# more stem:
	stem.left(90)
	stem.forward(60)

# drawing second leaf:
	stem.right(135)
	stem.forward(50)
	stem.left(45)
	stem.forward(50)
	stem.left(135)
	stem.forward(50)
	stem.left(45)
	stem.forward(50)

# more stem:
	stem.right(90)
	stem.forward(60)

def make_flower():
	epic_music()
	time.sleep(5)
	draw_petals()
	draw_stem()

make_flower()

window.exitonclick()