#!/usr/bin/env python2

#Asteroids by @TokyoEdTech / Written in Python 3.5
#Part 0: Demo
#Requires no external libraries (only standard modules)
#Use Left and Right arrow keys to rotate.
#Use Up Arrow to accelerate
#Use the down arrow to use hyperspace
#Use the space bar to fire your missile
#Video tutorials coming soon - keep an eye on www.christianthompson.com
import os
import random
import time
import math

#Import the Turtle module
import turtle
#Set the screensize
turtle.setup(width=800, height=800)
#Required by MacOSX to show the window
turtle.fd(0)
#Set the animations speed to the maximum
turtle.speed(0)
#Change the background color
turtle.bgcolor("black")
#Change the window title
turtle.title("Asteroids")
#Change the background image
#turtle.bgpic("starfield.gif")
#Hide the default turtle
turtle.ht()
#This saves memory
turtle.setundobuffer(1)
#This speeds up drawing
turtle.tracer(0)


class Shield(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.speed(0)
		self.penup()
		self.ht()
		self.frame = 1
		self.strength = 100

	def draw(self):
		shield.goto(player.xcor() + 20, player.ycor())
		shield.setheading(90)
		shield.pendown()
		if shield.strength > 66:
			shield.color("green")
			shield.pensize(3)
		elif shield.strength > 33 and shield.strength <= 66:
			shield.color("yellow")
			shield.pensize(2)
		elif shield.strength > 0 and shield.strength <= 33:
			shield.color("red")
			shield.pensize(1)
		else:
			shield.color("black")
			shield.strength = 0

		if self.strength > 0:
			shield.circle(20)
			shield.penup()
			shield.frame += 1
		else:
			shield.clear()

		if shield.frame == 3:
			shield.clear()
			shield.frame = 1




class Sprite(turtle.Turtle):
	def __init__(self, spriteshape, color, startx, starty):
		turtle.Turtle.__init__(self, shape = spriteshape)
		self.speed(0)
		self.penup()
		self.color(color)
		self.fd(0)
		self.goto(startx, starty)
		self.speed = 1

	def move(self):
		self.fd(self.speed)

		#Boundary detection
		if self.xcor() > 290:
			self.setx(self.xcor() - 580)

		if self.xcor() < -290:
			self.setx(self.xcor() + 580)

		if self.ycor() > 290:
			self.sety(self.ycor() - 580)

		if self.ycor() < -290:
			self.sety(self.ycor() + 580)

	def is_collision(self, other):
		#Distance changes based on shield strength
		if shield.strength > 0:
			if other.size == 3.0:
				distance = 45
			elif other.size == 2.0:
				distance = 35
			elif other.size == 1.0:
				distance = 25
		else:
			if other.size == 3.0:
				distance = 30
			elif other.size == 2.0:
				distance = 25
			elif other.size == 1.0:
				distance = 20


		if (self.xcor() >= (other.xcor() - distance)) and \
		(self.xcor() <= (other.xcor() + distance)) and \
		(self.ycor() >= (other.ycor() - distance)) and \
		(self.ycor() <= (other.ycor() + distance)):
			return True
		else:
			return False

class Player(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
		self.speed = 0
		self.lives = 3
		self.shapesize(stretch_wid=0.6, stretch_len=1.1, outline=None)
		self.thrust = 1
		self.dx = 0
		self.dy = 0
		self.rotation_speed = 0

	def turn_left(self):
		self.rotation_speed = 30
		h = self.heading() + self.rotation_speed
		player.setheading(h)

	def turn_right(self):
		self.rotation_speed = -30
		h = self.heading() + self.rotation_speed
		player.setheading(h)

	def accelerate(self):
		h = player.heading()
		self.dx += math.cos(h*math.pi/180)*self.thrust
		self.dy += math.sin(h*math.pi/180)*self.thrust

	def hyperspace(self):
		#os.system("afplay hyperspace.mp3&")
		x = random.randint(-250, 250)
		y = random.randint(-250, 250)
		self.goto(x, y)
		self.dx *= 0.5
		self.dy *= 0.5

	def move(self):
		player.goto(player.xcor()+self.dx, player.ycor()+self.dy)

		#Boundary detection
		if self.xcor() > 290:
			self.setx(self.xcor() - 580)

		if self.xcor() < -290:
			self.setx(self.xcor() + 580)

		if self.ycor() > 290:
			self.sety(self.ycor() - 580)

		if self.ycor() < -290:
			self.sety(self.ycor() + 580)

	def collides(self, asteroid):
		if shield.strength > 0:
			for particle in particles:
				x = (asteroid.xcor() + player.xcor()) / 2.0
				y = (asteroid.ycor() + player.ycor()) / 2.0
				particle.explode(x, y)
			asteroid.destroy()
			game.score += 100
			shield.strength -= int(10 * asteroid.size)
		else:
			for particle in particles:
				x = (asteroid.xcor() + player.xcor()) / 2.0
				y = (asteroid.ycor() + player.ycor()) / 2.0
				particle.explode(x, y)
			game.score -= 100
			game.lives -= 1

			#Check if player is out of lives. If so, reset.
			if game.lives < 1:
				#Reset game
				for asteroid in asteroids:
					asteroid.size = 1
					asteroid.goto(-1000, -1000)

				for asteroid in asteroids:
					asteroid.destroy()
				#Clear the asteroid list
				try:
					#Python 3.3 and above
					asteroids.clear()
				except:
					#Python 3.2 and below
					global asteroids
					asteroids = []

				game.level = 1
				game.lives = 3
				game.score = 0
				shield.strength = 100
				player.goto(0, 0)
				game.start_level()

			asteroid.destroy()

		game.show_status()


class Asteroid(Sprite):
	def __init__(self, spriteshape, color, size, speed, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.shapesize(stretch_wid=size, stretch_len=size, outline=None)
		self.speed = speed
		self.size = size
		self.setheading(random.randint(0,360))

	def move(self):
		self.fd(self.speed)

		if self.size == 3.0:
			left = -272
			right = 272
			top = 272
			bottom = -272

		elif self.size == 2.0:
			left = -280
			right = 280
			top = 289
			bottom = -280

		elif self.size == 1.0:
			left = -290
			right = 290
			top = 290
			bottom = -290


		#Boundary detection
		if self.xcor() > right:
			self.setx(self.xcor() - right * 2)

		if self.xcor() < left:
			self.setx(self.xcor() + right * 2)

		if self.ycor() > top:
			self.sety(self.ycor() - top * 2)

		if self.ycor() < bottom:
			self.sety(self.ycor() + top * 2)

	def destroy(self):
			if self.size == 3.0:
				self.size = 2.0
				self.speed = 5
				#Append a new asteroid
				asteroids.append(Asteroid("circle", "brown",2.0 ,4 , self.xcor(), self.ycor()))

				#Change Asteroid Size
				self.shapesize(stretch_wid=asteroid.size, stretch_len=asteroid.size, outline=None)
				#Change Heading
				self.setheading(random.randint(0, 360))


			elif self.size == 2.0:
				self.size = 1.0
				self.speed = 7
				#Append a new asteroid
				asteroids.append(Asteroid("circle", "brown",1.0 ,5 , self.xcor(), self.ycor()))

				#Change Asteroid Size
				self.shapesize(stretch_wid=asteroid.size, stretch_len=asteroid.size, outline=None)
				#Change Heading
				self.setheading(random.randint(0, 360))

			elif self.size == 1.0:
				self.goto(1000, 1000)
				self.ht()
				if asteroid in asteroids:
					asteroids.remove(asteroid)




class Missile(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.shapesize(stretch_wid=0.2, stretch_len=0.4, outline=None)
		self.speed = 20
		self.status = "ready"
		self.goto(-1000, 1000)

	def fire(self):
		if self.status == "ready":
			#Play missile sound
			#os.system("afplay laser.mp3&")
			self.goto(player.xcor(), player.ycor())
			self.setheading(player.heading())
			self.status = "firing"

	def move(self):
		if self.status == "ready":
			self.goto(-1000, 1000)

		elif self.status == "firing":
			self.fd(self.speed)

		#Border check
		if self.xcor() < -290 or self.xcor() > 290 or \
			self.ycor()< -290 or self.ycor()> 290:
			self.goto(-1000,1000)
			self.status = "ready"

class Particle(Sprite):
	def __init__(self, spriteshape, color, startx, starty):
		Sprite.__init__(self, spriteshape, color, startx, starty)
		self.shapesize(stretch_wid=0.1, stretch_len=0.1, outline=None)
		self.goto(-1000,-1000)
		self.frame = 0.0

	def explode(self, startx, starty):
		self.goto(startx,starty)
		self.setheading(random.randint(0,360))
		self.frame = 1.0
		self.myspeed = random.randint(2, 10)

	def move(self):
		if self.frame > 0:
			self.fd(self.myspeed)
			self.frame += 1.0
			self.shapesize(stretch_wid=0.3/self.frame, stretch_len=0.3/self.frame, outline=None)

		if self.frame > 15.0:
			self.frame = 0.0
			self.goto(-1000, -1000)

class Game():
	def __init__(self):
		self.level = 1
		self.score = 0
		self.state = "playing"
		self.pen = turtle.Turtle()
		self.lives = 3

	def start_level(self):
		for i in range(self.level):
			asteroids.append(Asteroid("circle", "brown", 3.0, 2, random.randint(-300, 300), random.randint(-300, 300)))

	def draw_border(self):
		#Draw border
		self.pen.speed(0)
		self.pen.color("white")
		self.pen.pensize(3)
		self.pen.penup()
		self.pen.goto(-300, 300)
		self.pen.pendown()
		for side in range(4):
			self.pen.fd(600)
			self.pen.rt(90)
		self.pen.penup()
		self.pen.ht()
		self.pen.pendown()

	def show_status(self):
		self.pen.undo()
		msg = "ASTEROIDS! Level: {}  Score: {}  Lives: {}  Shields: {}".format(self.level, self.score, game.lives, shield.strength)
		self.pen.penup()
		self.pen.goto(-300, 310)
		self.pen.write(msg, font=("Arial", 16, "normal"))



#Create my sprites
player = Player("triangle", "white", 0, 0)
missile = Missile("triangle", "yellow", 0, 0)
shield = Shield()

#Create game object
game = Game()

#Draw the game border
game.draw_border()

#Show the game status
game.show_status()

asteroids =[]

#Start the level
game.start_level()

particles = []
for i in range(25):
	particles.append(Particle("circle", random.choice(["yellow", "red", "orange"]), 0, 0))

#Keyboard bindings
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.hyperspace, "Down")
turtle.onkey(missile.fire, "space")
turtle.listen()

#Main game loop
while True:
	turtle.update()
	time.sleep(0.02)

	player.move()
	missile.move()

	for asteroid in asteroids:
		asteroid.move()

		#Check for a collision with the player
		if player.is_collision(asteroid):
			#Play explosion sound
			#os.system("afplay explosion.mp3&")
			#Do the explosion

			player.collides(asteroid)

		#Check for a collision between the missile and the asteroid
		if missile.is_collision(asteroid):
			#Play explosion sound
			#os.system("afplay explosion.mp3&")


			#Reset the Missile Status
			missile.status = "ready"

			#Increase the score
			game.score += 100
			game.show_status()
			#Do the explosion
			for particle in particles:
				x = (asteroid.xcor() + missile.xcor()) / 2.0
				y = (asteroid.ycor() + missile.ycor()) / 2.0
				particle.explode(x, y)

			#If the asteroid is Large, make it small times 2
			asteroid.destroy()

	for particle in particles:
		particle.move()

	#Shield
	shield.draw()

	#Check for end of level
	if len(asteroids) == 0:
		game.level += 1
		game.start_level()

	game.show_status()

delay = input("Press enter to finish. > ")
