from turtle import Turtle, Screen
import time

SCREEN_SIZE = (800, 600)
PADDLE_SHIFT = 0.85
TIME_DELAY = 0.1
PADDLE_SIZE = (20, 100)
PADDLE_SPEED = 50


def initialize(screen_size=(800, 600), paddle_shift=0.85, time_delay=0.1, paddle_size=(20, 80)):
    time_delay = time_delay
    paddle_size = paddle_size
    paddle_shift = paddle_shift
    screen_size = screen_size
    screen_object = Screen()
    screen_object.tracer(0)
    screen_object.setup(width=screen_size[0], height=screen_size[1])
    screen_object.bgcolor("black")
    screen_object.title("Pong Game v1.0")
    print("Initialization done successfully! Starting the game..")
    player_paddle_object(screen_object, time_delay, paddle_size, screen_size, paddle_shift)
    computer_paddle_object(screen_object, time_delay, paddle_size, screen_size, paddle_shift)
    print("Paddle's created!")
    screen_update(screen_object, time_delay)
    screen_object.exitonclick()
    return screen_object


def screen_update(screen_object, time_delay):
    time.sleep(time_delay)
    screen_object.update()


def player_paddle_object(screen_object, time_delay, paddle_size, screen_size, paddle_shift):
    global player_paddle_instance
    player_paddle_instance = Turtle()
    player_paddle_instance.color("white")
    player_paddle_instance.shape("square")
    player_paddle_instance.shapesize(stretch_len=int(paddle_size[0] / 20), stretch_wid=int(paddle_size[1] / 20))
    player_paddle_instance.penup()
    shift = int((screen_size[0] * paddle_shift) / 2)
    player_paddle_instance.goto(x=shift, y=0)
    screen_update(screen_object, time_delay)
    return player_paddle_instance


def computer_paddle_object(screen_object, time_delay, paddle_size, screen_size, paddle_shift):
    pc_paddle = Turtle()
    pc_paddle.color("white")
    pc_paddle.shape("square")
    pc_paddle.shapesize(stretch_len=int(paddle_size[0] / 20), stretch_wid=int(paddle_size[1] / 20))
    pc_paddle.penup()
    shift = int((screen_size[0] * paddle_shift) / -2)
    pc_paddle.goto(x=shift, y=0)
    screen_update(screen_object, time_delay)
    return pc_paddle


def paddle_up():
    global PADDLE_SPEED
    global player_paddle_instance
    player_paddle_instance.goto(x=player_paddle_instance.xcor(), y=player_paddle_instance.ycor() + PADDLE_SPEED)


def paddle_down():
    global PADDLE_SPEED
    global player_paddle_instance
    player_paddle_instance.goto(x=player_paddle_instance.xcor(), y=player_paddle_instance.ycor() + PADDLE_SPEED)


screen = initialize(screen_size=(800, 600), paddle_shift=0.85, time_delay=0.1, paddle_size=(20, 80))
player_paddle_instance = player_paddle_object(screen, TIME_DELAY, PADDLE_SIZE, SCREEN_SIZE, PADDLE_SHIFT)
computer_paddle = computer_paddle_object(screen, TIME_DELAY, PADDLE_SIZE, SCREEN_SIZE, PADDLE_SHIFT)
screen.listen()
screen.onkey(key="Up", fun=paddle_up)
screen.onkey(key="Down", fun=paddle_down)
