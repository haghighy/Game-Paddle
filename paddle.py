import turtle
import time
import random
import math

SCREEN_WIDTH=700
SCREEN_HEIGHT=700
v0=25
def init_screen():
    scrn=turtle.Screen()
    scrn.title('paddle game')
    scrn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    scrn.bgcolor('black')
    scrn.tracer(0)
    return scrn

def racket():
    rack=turtle.Turtle()
    rack.color('blue')
    xr=-0
    yr=-300
    rack.penup()
    rack.setpos(xr,yr)
    rack.shape('square')
    rack.shapesize(1,6)
    rack.direction="stop"
    return rack

def init_ball():
    b=turtle.Turtle()
    b.speed(0)
    b.shape('circle')
    b.color('red')
    b.shapesize(0.8,0.8)
    b.penup()
    b.goto(0,-280) 
    return b

def go_right():
    rack.direction="right"
def go_left():
    rack.direction="left"
    
def move_racket():
    xr,yr=rack.position()
    if rack.direction=="right":
        rack.setpos(xr+20,yr)
        rack.direction="ss"
    if rack.direction=="left":
        rack.setpos(xr-20,yr)
        rack.direction="ss"

def init_key_listener(s):
    s.listen()
    s.onkeypress(go_left,"Left")
    s.onkeypress(go_right,"Right")

def get_theta():
    theta=random.randint(20,160)
    return theta

def moving_ball1(b,theta):
    time=0.5
    vx=v0*math.cos(theta*(math.pi)/180)
    vy=v0*math.sin(theta*(math.pi)/180)
    xb,yb=b.position()
    xb=xb+vx*time
    yb=yb+vy*time
    b.setpos(xb,yb)

def init_blocks():
    xbl=-305
    ybl=310
    blocks=[]
    for i in range(7):
        block=turtle.Turtle()
        block.penup()
        block.setpos(xbl+i*100,ybl)
        block.shape('square')
        block.shapesize(1,3,20)
        block.color('lime')
        blocks.append(block)
    xbl=-290
    ybl=260    
    for i in range(7):
        block=turtle.Turtle()
        block.penup()
        block.setpos(xbl+i*100,ybl)
        block.shape('square')
        block.shapesize(1,3,20)
        block.color('dark turquoise')
        blocks.append(block)
    xbl=-305
    ybl=210    
    for i in range(7):
        block=turtle.Turtle()
        block.penup()
        block.setpos(xbl+i*100,ybl)
        block.shape('square')
        block.shapesize(1,3,20)
        block.color('medium violet red')
        blocks.append(block)
    xbl=-290
    ybl=160    
    for i in range(7):
        block=turtle.Turtle()
        block.penup()
        block.setpos(xbl+i*100,ybl)
        block.shape('square')
        block.shapesize(1,3,20)
        block.color('hot pink')
        blocks.append(block)
    return blocks


def check_border_x(b):
    xb,yb=b.position()
    if xb>=345 or xb<=-345:
        return True
    return False

def check_border_y():
    xb,yb=b.position()
    if yb>=345:
        return True
    return False


def check_blocks(b,bl,theta):
    collec=False
    xb,yb=b.position()
    if yb>150:
        for i in range(0,28):
            i=i
            xb2,yb2=bl[i].position()
            if abs(xb2-xb)<50 and abs(yb-yb2)<10:
                bl[i].setpos(1000,10)
                collec=True
                theta=-1*theta

    return collec

def racket_collision(b,rack,theta):
    xb,yb=b.position()
    xr,yr=rack.position()
    if abs(xb-xr)<=90 and abs(yb-yr)<=15:
        theta=-1* theta
    return theta

def lose(b):
    xb,yb=b.position()
    return yb<-345
def reset_game(rack,b):
    scrn=init_screen()
    xr=-0
    yr=-300
    rack.penup()
    rack.setpos(xr,yr)
    rack.direction="stop"
    b.penup()
    b.goto(0,-280)

def init_score_writer():
    pen=turtle.Turtle()
    pen.speed(0)
    pen.shape('square')
    pen.color('white')
    pen.penup()
    pen.hideturtle()
    return pen

def update_score():
    score_writer.undo()
    score_writer.hideturtle()
    score_writer.goto(-320,-330)
    score_writer.write("Score:{} High Score: {}".format(score,high_score), align="left", font=("Courier", 15, "normal"))
    
    
scrn=init_screen()
rack=racket()
b=init_ball()
theta=get_theta()
blocks=init_blocks()
score_writer=init_score_writer()
score=0
high_score=0
while True:
    move_racket()
    init_key_listener(scrn) 
    if rack.direction !="stop":
        if check_border_x(b):
            theta=180-theta
        if check_border_y():
            theta=-1*theta
        moving_ball1(b,theta)
        if check_blocks(b,blocks,theta):
            score+=1
            theta=-1*theta

        
        theta=racket_collision(b,rack,theta)
    if lose(b):
        scrn.clear()
        rack=racket()
        b=init_ball()
        blocks.clear()
        reset_game(rack,b)
        theta=get_theta()
        blocks=init_blocks()
        if score>high_score:
            high_score=score
        score=0
    update_score()
    scrn.update()
    time.sleep(0.02)

turtle.mainloop()
