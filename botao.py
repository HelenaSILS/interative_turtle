import turtle

class Botao:
    def __init__(self, cor, tamanho, s):
        self.cor = cor
        self.tamanho=tamanho
        self.s =s
    def desenha(self):
        turtle.begin_fill()
        turtle.color(self.cor)
        turtle.forward(self.tamanho)
        turtle.left(60)
        turtle.forward(self.tamanho)
        turtle.left(120)
        turtle.forward(self.tamanho)
        turtle.end_fill()
    def espiral(self):
        turtle.color(self.cor)
        for i in range(30):
            turtle.circle(3+i*2, 60)
    def arcoiris(self):
        self.s.colormode(255)
        for i in range(100):
            turtle.pencolor((200+i)%255,(255-i*2)%255,(i*10)%255)
            turtle.circle(3 + i * 2, 60)

