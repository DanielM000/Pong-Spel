from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(800, 600)
screen.title("Pong")
screen.bgcolor("black")
mittlinje = Turtle()

mittlinje.color("white")
mittlinje.penup()
mittlinje.goto(0, 300)
mittlinje.setheading(270)  # Pekar rakt neråt
mittlinje.pensize(3)

# Rita streckad linje
for _ in range(30):
    mittlinje.pendown()
    mittlinje.forward(10)
    mittlinje.penup()
    mittlinje.forward(10)

mittlinje.hideturtle()

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

# Poängturtlar
right_score_turtle = Turtle()
right_score_turtle.color("white")
right_score_turtle.penup()
right_score_turtle.hideturtle()
right_score_turtle.goto(200, 100)
r_score = 0
right_score_turtle.write(r_score, align="center", font=("Courier", 80, "normal"))

left_score_turtle = Turtle()
left_score_turtle.color("white")
left_score_turtle.penup()
left_score_turtle.hideturtle()
left_score_turtle.goto(-200, 100)
l_score = 0
left_score_turtle.write(l_score, align="center", font=("Courier", 80, "normal"))

def update_score_right():
    global r_score
    r_score += 1
    right_score_turtle.clear()
    right_score_turtle.goto(200, 100)
    right_score_turtle.write(r_score, align="center", font=("Courier", 80, "normal"))

def update_score_left():
    global l_score
    l_score += 1
    left_score_turtle.clear()
    left_score_turtle.goto(-200, 100)
    left_score_turtle.write(l_score, align="center", font=("Courier", 80, "normal"))

def visa_vinnare(text):
    vinnare_turtle = Turtle()
    vinnare_turtle.color("yellow")
    vinnare_turtle.penup()
    vinnare_turtle.hideturtle()
    vinnare_turtle.goto(0, 0)
    vinnare_turtle.write(text, align="center", font=("Courier", 20, "normal"))
    screen.update()
    time.sleep(5)

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
        update_score_left()  # Vänster spelare får poäng
        bollen.goto(0, 0)
        spelfigur1.goto(350, 0)
        spelfigur2.goto(-350, 0)
        screen.update()
        time.sleep(1)
        bollen.showturtle()
    
    # Miss vänster
    if bollen.xcor() < -380:
        bollen.hideturtle()
        update_score_right()  # Höger spelare får poäng
        bollen.goto(0, 0)
        spelfigur1.goto(350, 0)
        spelfigur2.goto(-350, 0)
        screen.update()
        time.sleep(1)
        bollen.showturtle()
    
    if r_score >= 10:
        visa_vinnare("Vi har en vinnare! Höger spelare!")
        game_is_on = False

    if l_score >= 10:
        visa_vinnare("Vi har en vinnare! Vänster spelare!")
        game_is_on = False




    screen.update()  # Uppdatera allt som har rört sig
    time.sleep(0.01)  # Smidig animation