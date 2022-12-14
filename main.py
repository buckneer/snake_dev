from snake import snake
import turtle

screen = turtle.Screen()
s = snake.Snake(screen)

s.write_word("ABVG]\\kmnoprst\'f;")
# s.typewriter_mode()

screen.mainloop()
