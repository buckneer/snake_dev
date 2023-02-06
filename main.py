from snake import snake
import turtle
from time import sleep

screen = turtle.Screen()

s = snake.Snake(screen)

s.write_word("Zdravo!")
sleep(1)
s.delete_every_letter()


screen.mainloop()
