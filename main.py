import turtle
import time
import botao
import os

t=turtle.Turtle()
s=turtle.Screen()
t.speed(50)
botao = botao.Botao("pink",50,s)

turtle.speed(1)
def mouse(x, y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    botao.desenha()


#botao.desenha()
s.onclick(mouse)
ts=turtle.getscreen()
ts.getcanvas().postscript(file="nnn.eps")


turtle.mainloop()

command = 'convert nnn.eps nnn.png'
os.system(command)