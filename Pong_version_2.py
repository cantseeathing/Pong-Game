import random
from turtle import Turtle, Screen
import time

SCREEN_SIZE = (800, 600)
PADDLE_SHIFT = 0.85
TIME_DELAY = 0.0001
PADDLE_SIZE = (20, 50)
PADDLE_SPEED = 30
BALL_SPEED = 3
POINT_LIMIT = 20


class Pong:
    def __init__(self, screen_size=(800, 600), paddle_shift=0.85, time_delay=0.1, paddle_size=(20, 80),
                 paddle_speed=50, ball_speed=100, point_limit=20):
        self.ball_x = None
        self.ball_y = None
        self.point_limit = point_limit
        self.player_2_score = 0
        self.player_1_score = 0
        self.score_board_2 = None
        self.score_board_1 = None
        self.game_limit_1 = None
        self.game_limit_2 = None
        self.game_over = False
        self.pause_banner_object = None
        self.ball_speed = ball_speed
        self.first_ball_kick = True
        self.ball_object = None
        self.game_on = False
        self.pc_paddle = None
        self.time_delay = time_delay
        self.paddle_size = paddle_size
        self.paddle_shift = paddle_shift
        self.player_paddle = None
        self.paddle_speed = paddle_speed
        self.screen_size = screen_size
        self.screen = Screen()
        self.screen.tracer(0)
        self.game_lock = True
        self.ball_speed_y = self.ball_speed
        self.ball_speed_x = self.ball_speed
        self.screen.setup(width=screen_size[0], height=screen_size[1])
        self.screen.bgcolor("black")
        self.screen.title("Pong Game v1.0")
        self.choice = int(self.screen.numinput(title="Pong",
                                               prompt="Please enter 1 for single player (BETA), or 2 for multiplayer",
                                               default=2, minval=1, maxval=2))
        if self.choice == 1:
            print("Initialization done successfully! Starting the SP game..")
        elif self.choice == 2:
            print("Initialization done successfully! Starting the MP game..")
        self.player_paddle_object()
        self.computer_paddle_object()
        self.game_bounds()
        self.score_banner()
        self.ball()
        print("Ball created successfully..")
        self.pause_banner()
        self.screen_update()

    def score_banner(self):
        self.score_board_1 = Turtle()
        self.score_board_2 = Turtle()
        self.score_board_1.penup()
        self.score_board_2.penup()
        self.score_board_1.hideturtle()
        self.score_board_2.hideturtle()
        self.score_board_1.color("white")
        self.score_board_2.color("white")
        self.score_board_1.goto(x=int((self.screen_size[0] / 2) * 0.95), y=int((self.screen_size[1] / 2) * 0.92))
        self.score_board_1.write(f"Player 1 score: {self.player_1_score}/{self.point_limit}", True, align="right",
                                 font=('Arial', 15, 'normal'))
        self.score_board_1.goto(x=int((self.screen_size[0] / 2) * -0.95), y=int((self.screen_size[1] / 2) * 0.92))
        self.score_board_1.write(f"Player 2 score: {self.player_2_score}/{self.point_limit}", True, align="left",
                                 font=('Arial', 15, 'normal'))

    def game_bounds(self):
        self.game_limit_1 = Turtle()
        self.game_limit_2 = Turtle()
        self.game_limit_1.penup()
        self.game_limit_2.penup()
        self.game_limit_1.color("white")
        self.game_limit_2.color("white")
        self.game_limit_1.shape("square")
        self.game_limit_2.shape("square")
        bounds_width = 10
        self.game_limit_1.shapesize(stretch_wid=bounds_width / 20, stretch_len=int(self.screen_size[0] / 20))
        self.game_limit_2.shapesize(stretch_wid=bounds_width / 20, stretch_len=int(self.screen_size[0] / 20))
        self.game_limit_1.goto(x=0, y=int((self.screen_size[1] / -2) * 0.9))
        self.game_limit_2.goto(x=0, y=int((self.screen_size[1] / 2) * 0.9))

    def pause_banner(self):
        self.pause_banner_object = Turtle()
        self.pause_banner_object.color("white")
        self.pause_banner_object.penup()
        self.pause_banner_object.hideturtle()
        self.pause_banner_object.goto(x=0, y=50)
        self.pause_banner_object.write("Press Space to start the game..", True, align="center",
                                       font=('Arial', 15, 'normal'))
        self.screen_update()
        self.game_on = False
        self.main_game()

    def screen_update(self):
        time.sleep(self.time_delay)
        self.screen.update()

    def main_game(self):
        self.screen.listen()
        self.screen.onkey(key="Up", fun=self.player_paddle_up)
        self.screen.onkey(key="Down", fun=self.player_paddle_down)
        self.screen.onkey(key="space", fun=self.game_stop)
        if self.choice == 2:
            self.screen.onkey(key="w", fun=self.player2_paddle_up)
            self.screen.onkey(key="s", fun=self.player2_paddle_down)
        while self.game_on:
            if self.choice == 1:
                self.computer_ai()
            self.ball_movement()

    def computer_ai(self):
        new_y = 0
        if self.ball_object.ycor() > self.pc_paddle.ycor():
            new_y = self.pc_paddle.ycor() + self.paddle_speed
            if new_y + int(0.5 * self.paddle_size[1]) < int(self.screen_size[1] / 2) and not self.game_lock:
                self.pc_paddle.goto(x=self.pc_paddle.xcor(), y=new_y)
                self.screen_update()
        else:
            new_y = self.pc_paddle.ycor() - self.paddle_speed
            if new_y + int(-0.5 * self.paddle_size[1]) > int(self.screen_size[1] / -2) and not self.game_lock:
                self.pc_paddle.goto(x=self.pc_paddle.xcor(), y=new_y)
                self.screen_update()

    def game_stop(self):
        if not self.game_on and self.game_lock:
            self.game_on = True
            self.game_lock = False
            self.pause_banner_object.clear()
            self.main_game()
        else:
            self.game_on = False
            self.game_lock = True
            self.pause_banner_object.goto(x=0, y=50)
            self.pause_banner_object.write("Game is paused, press Space to continue..", True, align="center",
                                           font=('Arial', 15, 'normal'))

    def player_paddle_object(self):
        self.player_paddle = Turtle()
        self.player_paddle.color("white")
        self.player_paddle.shape("square")
        self.player_paddle.shapesize(stretch_len=int(self.paddle_size[0] / 20),
                                     stretch_wid=int(self.paddle_size[1] / 20))
        self.player_paddle.penup()
        shift = int((self.screen_size[0] * self.paddle_shift) / 2)
        self.player_paddle.goto(x=shift, y=0)
        self.screen_update()

    def computer_paddle_object(self):
        self.pc_paddle = Turtle()
        self.pc_paddle.color("white")
        self.pc_paddle.shape("square")
        self.pc_paddle.shapesize(stretch_len=int(self.paddle_size[0] / 20), stretch_wid=int(self.paddle_size[1] / 20))
        self.pc_paddle.penup()
        shift = int((self.screen_size[0] * self.paddle_shift) / -2)
        self.pc_paddle.goto(x=shift, y=0)
        self.screen_update()

    def player_paddle_up(self):
        new_y = self.player_paddle.ycor() + self.paddle_speed
        if new_y + int(0.5 * self.paddle_size[1]) < int(self.screen_size[1] / 2) and not self.game_lock:
            self.player_paddle.goto(x=self.player_paddle.xcor(), y=new_y)
            self.screen_update()

    def player_paddle_down(self):
        new_y = self.player_paddle.ycor() - self.paddle_speed
        if new_y + int(-0.5 * self.paddle_size[1]) > int(self.screen_size[1] / -2) and not self.game_lock:
            self.player_paddle.goto(x=self.player_paddle.xcor(), y=new_y)
            self.screen_update()

    def player2_paddle_up(self):
        new_y = self.pc_paddle.ycor() + self.paddle_speed
        if new_y + int(0.5 * self.paddle_size[1]) < int(self.screen_size[1] / 2) and not self.game_lock:
            self.pc_paddle.goto(x=self.pc_paddle.xcor(), y=new_y)
            self.screen_update()

    def player2_paddle_down(self):
        new_y = self.pc_paddle.ycor() - self.paddle_speed
        if new_y + int(-0.5 * self.paddle_size[1]) > int(self.screen_size[1] / -2) and not self.game_lock:
            self.pc_paddle.goto(x=self.pc_paddle.xcor(), y=new_y)
            self.screen_update()

    def ball(self):
        self.ball_object = Turtle()
        self.ball_object.penup()
        self.ball_object.color("white")
        self.ball_object.shape("circle")
        self.ball_object.goto(0, 0)
        self.screen_update()

    def ball_movement(self):
        ball_distance = 30
        ball_paddle_factor = 0.8
        if self.first_ball_kick:
            self.ball_object.goto(x=0, y=0)
            self.first_ball_kick = False
        self.ball_x = self.ball_object.xcor() + self.ball_speed_x
        self.ball_y = self.ball_object.ycor() + self.ball_speed_y
        self.ball_object.goto(x=self.ball_x, y=self.ball_y)
        if self.ball_object.ycor() >= self.game_limit_2.ycor() * 0.95 or \
                self.ball_object.ycor() <= self.game_limit_1.ycor() * 0.95:
            print("wall bounce")
            self.bounce_y()
        if (self.ball_object.distance(self.player_paddle) < ball_distance and self.ball_object.xcor() >=
            int((self.screen_size[1] / 2) * ball_paddle_factor)) or (self.ball_object.distance(self.pc_paddle) <
                                                                     ball_distance and self.ball_object.xcor() <=
                                                                     int((self.screen_size[
                                                                              1] / -2) * ball_paddle_factor)):
            self.bounce_x()
            print("wall bounce")
        self.check_scoring()  # check if a player scored
        self.screen_update()
        self.game_over_check()  # check if the game is over

    def bounce_y(self):
        self.ball_speed_y = self.ball_speed_y * -1

    def bounce_x(self):
        self.ball_speed_x = self.ball_speed_x * -1

    def check_scoring(self):
        if self.ball_object.xcor() >= int(self.screen_size[0] / 2):
            print("Player 2 scored!")
            self.player_2_score += 1
            self.first_ball_kick = True
            self.score_board_1.clear()
            self.score_board_2.clear()
            self.score_banner()
        if self.ball_object.xcor() <= int(self.screen_size[0] / -2):
            print("Player 1 scored!")
            self.player_1_score += 1
            self.first_ball_kick = True
            self.score_board_1.clear()
            self.score_board_2.clear()
            self.score_banner()

    def game_over_check(self):
        if self.player_2_score >= self.point_limit:
            self.game_on = False
            self.pause_banner_object.clear()
            self.pause_banner_object.write("Game over, Player 2 won!", True, align="center",
                                           font=('Arial', 15, 'normal'))
        elif self.player_1_score >= self.point_limit:
            self.game_on = False
            self.pause_banner_object.clear()
            self.pause_banner_object.goto(x=0, y=0)
            self.pause_banner_object.write("Game over, Player 1 won!", True, align="center",
                                           font=('Arial', 15, 'normal'))


game = Pong(screen_size=SCREEN_SIZE, paddle_shift=PADDLE_SHIFT, time_delay=TIME_DELAY, paddle_size=PADDLE_SIZE,
            ball_speed=BALL_SPEED, paddle_speed=PADDLE_SPEED, point_limit=POINT_LIMIT)
# game.main_game()
game.screen.exitonclick()
