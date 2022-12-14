from snake import snake
import turtle

screen = turtle.Screen()
s = snake.Snake(screen)

s.write_word("PMF")
# s.typewriter_mode()

screen.mainloop()
