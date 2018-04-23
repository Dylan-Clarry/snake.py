import pygame
import sys
import random
import time

size = 500
frameRate = 22

class Snake():
	def __init__(self):
		# Initialize starting position, length, and direction
		self.position = [100, 50]
		self.body = [[100, 50], [90, 50], [80, 50]]
		self.direction = "DOWN"
		self.changeDirection = self.direction

	# Changes direction of the snake
	def changeDirectionTo(self, dir):
		if dir == "RIGHT" and not self.direction =="LEFT":
			self.direction = "RIGHT"
		if dir == "LEFT" and not self.direction =="RIGHT":
			self.direction = "LEFT"
		if dir == "UP" and not self.direction =="DOWN":
			self.direction = "UP"
		if dir == "DOWN" and not self.direction =="UP":
			self.direction = "DOWN"

	# Update position
	def move(self, foodPos):
		if self.direction == "RIGHT":
			self.position[0] += 10
		if self.direction == "LEFT":
			self.position[0] -= 10
		if self.direction == "UP":
			self.position[1] -= 10
		if self.direction == "DOWN":
			self.position[1] += 10
		self.body.insert(0, list(self.position))

		if self.position == foodPos:
			return 1
		else:
			self.body.pop()
			return 0

	def checkSelfCollision(self):
		if self.position[0] > 500 or self.position[0] < 0:
			return 1
		elif self.position[1] > 500 or self.position[1] < 0:
			return 1
		for bodyPart in self.body[1:]:
			if self.position == bodyPart:
				return 1
		return 0

	def getHeadPos(self):
		return self.position

	def getBody(self):
		return self.body

class Food():
	def __init__(self):
		self.position = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
		self.isOnScreen = True

	def spawnFood(self):
		if self.isOnScreen == False:
			self.position = [random.randrange(1, 50) * 10, random.randrange(1, 50) * 10]
			self.isOnScreen = True
		return self.position

	def setFoodOnScreen(self, i):
		self.isOnScreen = i

window = pygame.display.set_mode((size, size))
pygame.display.set_caption("Snake.py")
fps = pygame.time.Clock()

# Set score to 0
score = 0

# Create snake and food
snake = Snake()
food = Food()

def gameOver():
	pygame.quit()
	sys.exit()

while True:
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			gameOver()
		elif e.type == pygame.KEYDOWN:
			if e.key == pygame.K_RIGHT:
				snake.changeDirectionTo("RIGHT")
			if e.key == pygame.K_LEFT:
				snake.changeDirectionTo("LEFT")
			if e.key == pygame.K_UP:
				snake.changeDirectionTo("UP")
			if e.key == pygame.K_DOWN:
				snake.changeDirectionTo("DOWN")

	foodPos = food.spawnFood()
	if snake.move(foodPos) == 1:
		score = 1
		food.setFoodOnScreen(False)

	window.fill(pygame.Color(0, 0, 0))
	for pos in snake.getBody():
		pygame.draw.rect(window, pygame.Color(0, 225, 0), pygame.Rect(pos[0], pos[1], 9, 9))
	pygame.draw.rect(window, pygame.Color(225, 0, 0), pygame.Rect(foodPos[0], foodPos[1], 10, 10))
	if(snake.checkSelfCollision() == 1):
		gameOver()
	pygame.display.set_caption("Snake.py | Score: " + str(score))
	pygame.display.flip()
	fps.tick(frameRate)