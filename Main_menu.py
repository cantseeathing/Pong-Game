import turtle


class MainScreen:
    def __init__(self, scree_size=(800, 600)):
        self.screen = turtle.Screen()
        self.screen.setup(width=scree_size[0], height=scree_size[1])
        self.screen.bgcolor("black")
        self.screen.title("Pong Game v1.0")
        print("Initialization done successfully! Starting the game..")
        self.screen.exitonclick()
