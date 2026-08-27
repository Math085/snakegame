import turtle

#tela
direçao = "direita"
tela = turtle.Screen()
tela.setup(width=800, height=600)
tela.title("Snake Game")
tela.bgcolor("green")

tela.update()

#cabeça da cobra

cabeça = turtle.Turtle()
cabeça.shape("square")
cabeça.color("blue")
cabeça.penup()
cabeça.goto(0, 0)
cabeça.speed(0)

#corpo da cobra
corpo = []

for i in range(2):
    segmento = turtle.Turtle()
    segmento.shape("square")
    segmento.color("blue")
    segmento.penup()
    segmento.goto(-20 * (i +1), 0)
    segmento.speed(0)
    corpo.append(segmento)


#comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(0, 100)

def mover():
    #corpo segue
    for i in range(len(corpo) - 1, 0, -1):
        corpo[i].goto(corpo[i - 1].xcor(),corpo[i - 1].ycor())

    if len(corpo) > 0:
        corpo[0].goto(cabeça.xcor(),cabeça.ycor())

    #direçao do corpo

    if direçao == "cima":
        cabeça.setheading(90)

    elif direçao == "baixo":
        cabeça.setheading(270)

    elif direçao == "esquerda":
        cabeça.setheading(180)

    elif direçao == "parado":
        cabeça.setheading(0)

    cabeça.forward(20)

    if cabeça.distance(comida) < 20:
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        comida.goto(x, y)

        #segmento ao corpo
        novo_segmento = turtle.Turtle()
        novo_segmento.speed(0)
        novo_segmento.shape("square")
        novo_segmento.color("grey")
        novo_segmento.penup()
        corpo.append(novo_segmento)

    tela.ontimer(mover, 150)

mover()





#movimento

def cima():
    global direçao
    if direçao != "baixo":
        direçao = "cima"

def baixo():
    global direçao
    if direçao != "cima":
        direçao = "baixo"
    

def esquerda():
    global direçao
    if direçao != "direita":
        direçao = "esquerda"
    

def direita():
    global direçao
    if direçao != "esquerda":
        direçao = "direita"



import random




#controle

tela.listen()
tela.onkeypress(cima, "Up")
tela.onkeypress(baixo, "Down")
tela.onkeypress(esquerda, "Left")
tela.onkeypress(direita, "Right")

#loop
tela.mainloop()