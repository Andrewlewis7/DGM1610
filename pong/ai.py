from paddle import Paddle
from ball import Ball

class AI:
	def __init__(self, striker, ball):
		self.striker = striker
		self.ball = ball
		self.height = striker.height

	def move(self, ball):
		if ball.posy < (self.striker.posy):
			return -1
		elif ball.posy > (self.striker.posy + self.height):
			return 1
		else:
			return 0

	def update(self):
		YFac = self.move(self.ball)
		self.striker.update(YFac)