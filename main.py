from Pong import Pong

SCREEN_SIZE = (800, 600)
PADDLE_SHIFT = 0.85
TIME_DELAY = 0.1
PADDLE_SIZE = (20, 100)
PADDLE_SPEED = 50

game = Pong(screen_size=SCREEN_SIZE, paddle_shift=PADDLE_SHIFT, time_delay=TIME_DELAY, paddle_size=PADDLE_SIZE)
game.screen.listen()


