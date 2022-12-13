from snake import snake
import turtle

screen = turtle.Screen()
s = snake.Snake(screen)
#
# screen.onkeyrelease(s.delete_letter, 'BackSpace')
#
# characters = ['a', 'b', 's']
# for key in characters:
#     screen.onkeyrelease(lambda key = key: s.type_letter(key), key)
#
# screen.listen()

# input = turtle.textinput('Input', 'Your text goes here:')
input = "ab"
arr = list(input.lower())

for item in arr:
    s.type_letter(item)

screen.mainloop()



steps = {"a": [
    {""}
]}