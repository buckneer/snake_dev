import turtle
from .utils import generate_letters
from time import sleep


class Snake:

    def __init__(self, screen, width=1000, height=400):
        self.shapes = []
        self.next_step = 0
        self.height = height
        self.width = width
        self.screen = screen
        self.letter_width = 50
        self.letter_height = self.letter_width * 2
        self.start_point = {"x": 0, "y": 0}
        self.steps = {}
        self.row = 0
        self.move_factor = 0
        self.y = 0

        self.screen.setup(width, height)

    def typewriter_mode(self):
        self.screen.onkeyrelease(self.delete_letter, 'BackSpace')
        characters = ['a', 'b', 'v', 'g', ']', '\\', 'k', 'm', 'n', 'o', 'p', 'r', 's', 't', '\'', 'f', ';']
        self.start_point["x"] = -1 * (self.width / 2.5)
        self.start_point["y"] = (self.height / 2.5) - self.letter_height
        for key in characters:
            self.screen.onkeyrelease(lambda key = key: self.type_letter(key), key)

        self.screen.listen()
        pass

    def write_word(self, word):

        arr = self.get_starting_point(word)

        for item in arr:
            self.type_letter(item)

    def delete_letter(self):

        if len(self.shapes):
            self.shapes[-1].clear()
            del self.shapes[-1]

    def get_starting_point(self, word):
        arr = list(word.lower())
        half = len(arr) // 2

        if len(arr) % 2 == 0:
            self.start_point["x"] = -1 * (half * self.letter_width)
        else:
            self.start_point["x"] = -1 * (half * self.letter_width) - 25

        return arr

    def type_letter(self, letter):

        # y = ((self.letter_height + self.letter_width) * -1) * self.row
        y = self.start_point["y"]



        if len(self.shapes) == 0:
            x = self.start_point["x"]
        else:
            x = self.start_point["x"] + (self.letter_width * 1.2) * self.move_factor

        self.move_factor += 1
        self.shapes.append(turtle.Turtle())

        if len(self.shapes) % 11 == 0 and not len(self.shapes) == 0:
            self.start_point["y"] += (self.letter_height + self.letter_width) * -1
            self.move_factor = 0
        self.shapes[-1].speed(0)

        self.steps = generate_letters(x, y)
        self.translate(letter, self.shapes[-1])


    def translate(self, letter, turtle_object: turtle.Turtle):

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

