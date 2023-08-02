from paddle import Paddle
from ball import Ball

class AI:
    def __init__(self, paddle, ball):
        self.paddle = paddle(Paddle)
        self.ball = ball(Ball)

    def move(self, ball):
        if ball.posy < self.paddle.posy and self.paddle.posy > 0:
            return -1
        elif ball.posy > self.paddle.posy and self.paddle.posy < 400:
            return 1

    def update(self):
        YFac = self.move(self.ball)
        self.paddle.update(YFac)