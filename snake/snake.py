import turtle
from .utils import generate_letters, generate_letters_width, get_letter_width
from time import sleep
import os


class Snake:

    def __init__(self, screen, letter_width = 50, width=1000, height=400):
        self.shapes = []
        self.next_step = 0
        self.height = height
        self.width = width
        self.screen = screen
        self.letter_width = letter_width
        self.letter_height = self.letter_width * 2
        self.start_point = {"x": 0, "y": 0}
        self.steps = {}
        self.row = 0
        self.row_letters = 12
        self.move_factor = 0
        self.y = 0
        self.last_letter_width = 0
        self.letter_offset = 0
        self.word_width = 0
        self.screen.setup(width, height)
        self.create_UI()
        self.generateFontWidthBasedOnScreenWidth(self.width, self.letter_width)

    def typewriter_mode(self):
        self.screen.onkeyrelease(self.delete_letter, 'BackSpace')
        characters = ['a', 'b', 'v', 'g', ']', '\\', 'k', 'm', 'n', 'o', 'p', 'r', 's', 't', '\'', 'f', ';']
        self.start_point["x"] = -1 * (self.width / 2.5)
        self.start_point["y"] = (self.height / 2.5) - self.letter_height
        for key in characters:
            self.screen.onkeyrelease(lambda key = key: self.type_letter(key), key)

        self.screen.listen()
        pass

    def get_width_of_each_letter(self, word):
        word_array = list(word.lower())
        arr = []
        different_letters = generate_letters_width(self.letter_width)

        for letter in word_array:
            if (letter in different_letters):
                arr.append(different_letters[letter])
            else:
                arr.append(self.letter_width)

        return arr

    def write_word(self, word):
        arr = self.get_starting_point(word)
        
        for item in arr:
            self.type_letter(item)

    def delete_letter(self):

        if len(self.shapes):
            self.shapes[-1].clear()
            del self.shapes[-1]

    def get_starting_point(self, word):
        word_arr = list(word.lower())
        arr = self.get_width_of_each_letter(word)
        first_word_width = 0

        if len(arr) >= self.row_letters:
            for i in range(self.row_letters):
                first_word_width += arr[i] + (arr[i] * 0.66)
        else:
            for i in arr:
                first_word_width += i + (i * 0.66)

        half = (first_word_width) / 2
        self.start_point['x'] = -half

        print(first_word_width)
        return word_arr

    def type_letter(self, letter):

        x = self.start_point["x"] + self.word_width * self.move_factor
        y = self.start_point["y"]

        self.move_factor = 1
        self.shapes.append(turtle.Turtle())

        if len(self.shapes) % self.row_letters == 0 and not len(self.shapes) == 0:
            self.start_point["y"] -= (self.letter_height + self.letter_width)
            self.move_factor = 0
            self.word_width = 0

        self.shapes[-1].speed(0)

        self.steps = generate_letters(x, y, self.letter_width, self.letter_height)
        self.translate(letter, self.shapes[-1])
        
        if len(self.shapes) % self.row_letters != 0 and len(self.shapes) != 0:
            self.word_width += get_letter_width(letter) + (get_letter_width(letter) / 5)

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

    def change_font_size_by(self, font_change_value):

        if self.letter_width + font_change_value >= 0 and len(self.shapes) == 0:
            self.letter_width = self.letter_width + font_change_value
            self.letter_height = self.letter_width * 2

    def delete_every_letter(self):

        for i in range(len(self.shapes)):
            self.delete_letter()

        self.start_point = {"x": 0, "y": 0}
        self.row = 0
        self.move_factor = 0
        self.y = 0
        self.word_width = 0

    def add_input(self):
        self.write_word(turtle.textinput("Унос", "Унесите Ваш унос:"))

    def create_UI(self):
        icon_width = 30

        path = os.getcwd().replace('\\', '/') + '/snake/images/'

        trashcan_gif = path + 'delete.gif'
        input_gif = path + 'input.gif'

        self.screen.addshape(trashcan_gif)
        delete_icon = turtle.Turtle()
        delete_icon.shape(trashcan_gif)
        delete_icon.speed(0)
        delete_icon.penup()
        delete_icon.setpos(40, (self.height / 2) - icon_width)
        delete_icon.onclick(lambda x, y: self.delete_every_letter())

        self.screen.addshape(input_gif)
        input_icon = turtle.Turtle()
        input_icon.shape(input_gif)
        input_icon.speed(0)
        input_icon.penup()
        input_icon.setpos(-40, (self.height / 2) - icon_width)
        input_icon.onclick(lambda x, y: self.add_input())

    def generateFontWidthBasedOnScreenWidth(self, screenWidth, currentLetterWidth):
        max_width = max(generate_letters_width(currentLetterWidth).values())
        max_width_new = max_width
        if(max_width * 12 > (screenWidth * 0.7)):
            while(max_width_new * 12 > (screenWidth * 0.7)):
                max_width_new -= 1

            ratio = max_width_new / max_width 
            
            self.letter_width = self.letter_width * ratio
            self.letter_height = self.letter_width * 2
