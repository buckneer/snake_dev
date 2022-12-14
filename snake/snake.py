import turtle
from .utils import generate_letters


class Snake:

    def __init__(self, screen, width=800, height=800):
        self.shapes = []
        self.next_step = 0
        self.height = height
        self.width = width
        self.screen = screen
        self.steps = {}

        self.screen.setup(width, height)

    def delete_letter(self):

        if len(self.shapes):
            self.shapes[-1].clear()
            del self.shapes[-1]

    def type_letter(self, letter):
        width = 50
        height = width * 2

        self.shapes.append(turtle.Turtle())
        self.shapes[-1].speed(0)

        x = (width * 1.2) * len(self.shapes)
        y = 0

        self.steps = generate_letters(x, y)
        print(x)
        self.translate(letter, self.shapes[-1])


    def translate(self, letter, turtle_object: turtle.Turtle, width=50, height=100):

        current_letter = self.steps[letter]

        for step in current_letter:
            for item in step:
                if item == "draw":
                    x = step[item]["x"]
                    y = step[item]["y"]

                    turtle_object.setpos(x, y)
                elif item == "break":
                    x = step[item]["x"]
                    y = step[item]["y"]
                    turtle_object.penup()
                    turtle_object.setpos(x, y)
                    turtle_object.pendown()
                elif item == "circle":
                    angle = step[item]['angle']
                    radius = step[item]['radius']

                    if "rotation" in step[item]:
                        rotation = step[item]['rotation']

                        if rotation > 0:
                            turtle_object.right(rotation)
                        else:
                            turtle_object.left(rotation)

                    turtle_object.circle(radius, angle)

        turtle_object.hideturtle()

