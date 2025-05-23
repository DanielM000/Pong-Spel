from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(800, 600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)  # Manuell uppdatering

# Höger spelare
spelfigur1 = Turtle()
spelfigur1.shape("square")
spelfigur1.shapesize(6, 1)
spelfigur1.color("white")
spelfigur1.penup()
spelfigur1.setposition(350, 0)

def spelfigur1_up():
    if spelfigur1.ycor() < 250:
        spelfigur1.sety(spelfigur1.ycor() + 40)

def spelfigur1_down():
    if spelfigur1.ycor() > -250:
        spelfigur1.sety(spelfigur1.ycor() - 40)

# Vänster spelare
spelfigur2 = Turtle()
spelfigur2.shape("square")
spelfigur2.shapesize(6, 1)
spelfigur2.color("white")
spelfigur2.penup()
spelfigur2.setposition(-350, 0)

def spelfigur2_up():
    if spelfigur2.ycor() < 250:
        spelfigur2.sety(spelfigur2.ycor() + 30)

def spelfigur2_down():
    if spelfigur2.ycor() > -250:
        spelfigur2.sety(spelfigur2.ycor() - 30)

# Bollen
bollen = Turtle()
bollen.shape("circle")
bollen.color("white")
bollen.penup()

boll_dx = 3
boll_dy = 3
time.sleep(0.01)

# Tangentbindningar
screen.listen()
screen.onkey(spelfigur1_up, "Up")
screen.onkey(spelfigur1_down, "Down")
screen.onkey(spelfigur2_up, "w")
screen.onkey(spelfigur2_down, "s")

game_is_on = True
while game_is_on:
    # Flytta bollen
    bollen.setx(bollen.xcor() + boll_dx)
    bollen.sety(bollen.ycor() + boll_dy)

    # Kollision med väggar
    if bollen.ycor() > 290 or bollen.ycor() < -290:
        boll_dy *= -1

    # Kollision med spelare
    if bollen.xcor() > 320 and bollen.distance(spelfigur1) < 50:
        boll_dx *= -1

    if bollen.xcor() < -320 and bollen.distance(spelfigur2) < 50:
        boll_dx *= -1

    # Miss höger
    if bollen.xcor() > 380:
        bollen.hideturtle()
        bollen.goto(0, 0)
        spelfigur1.goto(350, 0)
        spelfigur2.goto(-350, 0)
        screen.update()
        time.sleep(1)
        bollen.showturtle()

    # Miss vänster
    if bollen.xcor() < -380:
        bollen.hideturtle()
        bollen.goto(0, 0)
        spelfigur1.goto(350, 0)
        spelfigur2.goto(-350, 0)
        screen.update()
        time.sleep(1)
        bollen.showturtle()

    screen.update()  # Uppdatera allt som har rört sig
    time.sleep(0.01)  # Smidig animation