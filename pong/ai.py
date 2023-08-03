from paddle import Paddle
from ball import Ball
from enum import Enum
import random
class AI:
	Difficulty = Enum('Difficulty', ['EASY', 'MEDIUM', 'HARD'])

	striker: Paddle
	ball: Ball
	height: float
	difficulty: Difficulty

	def __init__(self, striker, ball, difficulty):
		self.striker = striker
		self.ball = ball
		self.height = striker.height
		self.difficulty = difficulty
		self.random_error = 0

	def move(self, ball, random_error):
		if ball.posy < (self.striker.posy + random_error):
			return -1
		elif ball.posy > (self.striker.posy + self.height + random_error):
			return 1
		else:
			return 0

	def update(self):
		# print(f"Error: {self.random_error}")
		if self.difficulty == 'EASY':
			self.random_error = self.__clamp(self.random_error + random.randint(-3, 3), -20, 20)
		elif self.difficulty == 'MEDIUM':
			self.random_error = self.__clamp(self.random_error + random.randint(-2, 2), -15, 15)
		else:
			self.random_error = self.__clamp(self.random_error + random.randint(-1, 1), -10, 10)
		YFac = self.move(self.ball, self.random_error)
		self.striker.update(YFac)
	
	def reset(self):
		self.random_error = 0
	
	def __clamp(self, n, min, max):
		if n < min:
			return min
		elif n > max:
			return max
		else:
			return n
