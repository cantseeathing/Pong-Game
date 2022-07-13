import random
from turtle import Turtle


class Paddles:
    def __init__(self, screen_size, paddle_shift=0.1):
        self.screen_size = screen_size
        self.player_paddle = Turtle()
        self.player_paddle.color("white")
        self.player_paddle.hideturtle()
        self.player_paddle.penup()
        self.paddle_shift = paddle_shift
        #self.player_paddle.goto(x=int((self.screen_size[0]/2)*paddle_shift), y=0)
