###Kevin Daniel
###01/21/2020
###culminating.py
###Python Turtle Game

import turtle
import time
import random

while True:
    z = input('Press enter to start, H for help, and Q to quit: ')
    if z.lower() == 'h':
        print('This program is a 2D-Platformer where the user takes control of a grey cube, and its goal is to scale the various platforms while avoiding the triangle enemies to reach the top of the platform and obtain the treasure.')
    if z.lower() == 'q':
        exit()
    else:
        print('The Game Will Start...')
        break
    
#background
ba=turtle.Screen()
ba.bgcolor('black')
ba.setup(800,800)
ba.title('Le Game')
ba.tracer(1)

#white border
border = turtle.Turtle()
border.speed(0)
border.color('white')
border.penup()
border.setposition(-300,-300)
border.pendown()
border.pensize(4)
for loop in range(4): #600 X 600 playing space 
    border.fd(600)
    border.lt(90)
border.hideturtle()

#blue box 
player = turtle.Turtle()
player.shape('square')
player.color('grey')
player.penup()
player.setpos(0,-287)

#platform
platform = turtle.Turtle()
platform.color('white')
platform.shape('square')
platform.shapesize(1,3,1)
platform.penup()
platform.setposition(0,-254)


#platform 2
platform2 = turtle.Turtle()
platform2.color('white')
platform2.shape('square')
platform2.shapesize(1,3,1)
platform2.penup()
platform2.setposition(-90,-206)

#platform 3
platform3 = turtle.Turtle()
platform3.color('white')
platform3.shape('square')
platform3.shapesize(1,3,1)
platform3.penup()
platform3.setposition(90,-203)

#platform 4
platform4 = turtle.Turtle()
platform4.color('white')
platform4.shape('square')
platform4.shapesize(1,3,1)
platform4.penup()
platform4.setposition(180,-152)

#platform 5
platform5 = turtle.Turtle()
platform5.color('white')
platform5.shape('square')
platform5.shapesize(1,3,1)
platform5.penup()
platform5.setposition(-180,-149)

#platform 6
platform6 = turtle.Turtle()
platform6.color('white')
platform6.shape('square')
platform6.shapesize(1,3,1)
platform6.penup()
platform6.setposition(0,-161)

#platform 7
platform7 = turtle.Turtle()
platform7.color('white')
platform7.shape('square')
platform7.shapesize(1,3,1)
platform7.penup()
platform7.setposition(-90,-107)

#platform 8
platform8 = turtle.Turtle()
platform8.color('white')
platform8.shape('square')
platform8.shapesize(1,3,1)
platform8.penup()
platform8.setposition(90,-105)

#platform 9
platform9 = turtle.Turtle()
platform9.color('white')
platform9.shape('square')
platform9.shapesize(1,3,1)
platform9.penup()
platform9.setposition(-180,-68)

#platform 10
platform10 = turtle.Turtle()
platform10.color('white')
platform10.shape('square')
platform10.shapesize(1,3,1)
platform10.penup()
platform10.setposition(180,-65)

#platform 11
platform11 = turtle.Turtle()
platform11.color('white')
platform11.shape('square')
platform11.shapesize(1,11,1)
platform11.penup()
platform11.setposition(0,-32)

#platform 12
platform12 = turtle.Turtle()
platform12.color('white')
platform12.shape('square')
platform12.shapesize(1,7,1)
platform12.penup()
platform12.setposition(-200,34)

#platform 13
platform12 = turtle.Turtle()
platform12.color('white')
platform12.shape('square')
platform12.shapesize(1,7,1)
platform12.penup()
platform12.setposition(200,37)

#platform 14
platform14 = turtle.Turtle()
platform14.color('white')
platform14.shape('square')
platform14.shapesize(1,7,1)
platform14.penup()
platform14.setposition(0,67)

#Treasure
treasure = turtle.Turtle()
treasure.color('gold')
treasure.shape('square')
treasure.penup()
treasure.setposition(0,88)

#enemy
enemy = turtle.Turtle()
enemy.color('red')
enemy.shape('triangle')
enemy.setheading(90)
enemy.penup()
enemy.setposition(-150,51)

#second enemy 
enemy2 = turtle.Turtle()
enemy2.color('red')
enemy2.shape('triangle')
enemy2.setheading(90)
enemy2.penup()
enemy2.setposition(150,54)

#third enemy 
en = turtle.Turtle()
en.color('red')
en.shape('triangle')
en.setheading(90)
en.penup()
en.setposition(-45,-15)

#fourth enemy; even though the variable says otherwise
enemythree = turtle.Turtle()
enemythree.color('red')
enemythree.shape('triangle')
enemythree.setheading(90)
enemythree.penup()
enemythree.setposition(45,-15)

#treasure to vanish
def vanish():
    treasure.hideturtle() #so the treasure will dissapear showing the user that they have "obtained" the treasure
    text = turtle.Turtle()
    text.penup()
    text.setposition(0,150)
    text.color('white')
    style = ('Arial',20,'bold')
    text.write('YOU HAVE GOT THE TREASURE...YOU WIN',font=style,align='center')
    text.hideturtle()
    time.sleep(3)
    ba.bye()#closes the turtle window
    exit() #then proceeds to close the 

#collision with enemy
def collision_enemy4():
    if player.ycor() == -11:
        if player.xcor() == enemythree.xcor():
            txt = turtle.Turtle() #the final text that will appear 
            txt.penup()
            txt.setposition(0,150)
            txt.color('white')
            sty = ('Arial',20,'bold')
            txt.write('YOU HAVE DIED...GAME OVER',font=sty,align='center')
            txt.hideturtle()
            time.sleep(3) #to give the user time to see the message that they died
            ba.bye() 
            exit()

def collision_enemy3(): #repeated for each enemy and their unique x and  y coordinate 
    if player.ycor() == -11:
        if player.xcor() == en.xcor():
            txt = turtle.Turtle()
            txt.penup()
            txt.setposition(0,150)
            txt.color('white')
            sty =  ('Arial',20,'bold')
            txt.write('YOU HAVE DIED...YOU LOSE GAME OVER',font=sty,align='center')
            txt.hideturtle()
            time.sleep(3)
            ba.bye()
            exit()

def collision_enemy2():
    if player.ycor() == 58:
        if player.xcor() == enemy2.xcor():
            txt = turtle.Turtle() 
            txt.penup()
            txt.setposition(0,150)
            txt.color('white')
            sty =  ('Arial',20,'bold')
            txt.write('YOU HAVE DIED...YOU LOSE GAME OVER',font=sty,align='center')
            txt.hideturtle()
            time.sleep(3)
            ba.bye()
            exit()
    
def collision_enemy():
    if player.ycor() == 55:
        if player.xcor() == enemy.xcor():
            txt = turtle.Turtle()
            txt.penup()
            txt.setposition(0,150)
            txt.color('white')
            sty =  ('Arial',20,'bold')
            txt.write('YOU HAVE DIED...YOU LOSE GAME OVER',font=sty,align='center')
            txt.hideturtle()
            time.sleep(2)
            ba.bye() 
            exit() 
            
#collision with treasure
def collision():
    if player.ycor() == 88:
        if player.xcor() == 0:
            vanish()
    if player.ycor() == 88:
        if player.xcor() == -15:
            vanish()
    if player.ycor() == 88:
        if player.xcor() == 15:
            vanish()            
 
#movement
def left():
    move_left = player.xcor() - 15 #moving left or right always by 15 pixels
    player.setx(move_left)
    if move_left < -285: #if the current x cord + another move is greater than the boundary then set it back to the boundary, so the player cannot escape the map
       player.setx(-285) 
    collision()
    if player.ycor() == 88 and player.xcor() not in range(-75,90) or player.ycor() == 55 and player.xcor() not in range(-270,-120) or player.ycor() == 58 and player.xcor() not in range(120,270) or player.ycor() == -11 and player.xcor() not in range(-105,120) or player.ycor() == -44 and player.xcor() not in range(150,210) or player.ycor() == -47 and player.xcor() not in range(-210,-135) or player.ycor() == -83 and player.xcor() not in range(60,135) or player.ycor() == -86 and player.xcor() not in range (-120,-45) or player.ycor() == -140 and player.xcor() not in range (-35,35) or player.ycor() == -128 and player.xcor() not in range(-210,-140) or player.ycor() == - 131 and player.xcor() not in range (150,220) or player.ycor() == -182 and player.xcor() not in range(60,130) or player.ycor() == -233 and player.xcor() not in range(-35,35) or player.ycor() == -185 and player.xcor() not in range(-120,-50):
        while player.ycor() != -287:
            move_jump = player. ycor() - 3
            player.sety(move_jump)
            time.sleep(0) #this long code constantly checks if there is another platform under to land on rather than going straight through
            if player.ycor() == -287 or player.ycor() == -233 and player.xcor() in range (-35,35) or player.ycor() == -185 and player.xcor() in range (-120,-50) or player.ycor() == -182 and player.xcor() in range (60,130) or player.ycor() == - 131 and player.xcor() in range (150,220) or player.ycor() == - 128 and player.xcor() in range(-210,-140) or player.ycor() == -140 and player.xcor() in range(-35,35) or player.ycor() == - 86 and  player.xcor() in range(-120,-45) or player.ycor() == -83 and player.xcor() in range(60,135) or player.ycor() == -47 and player.xcor() in range(-210,-135) or player.ycor() == -44 and player.xcor() in range (150,210) or player.ycor() == -11 and player.xcor() in range(-120,120) or player.ycor() == 58 and player.xcor() in range(120,270) or player.ycor() == 55 and player.xcor() in range(-270,-120) or player.ycor() == 88 and player.xcor() in range(-75,90):
                break 
   
def right():
    move_right = player.xcor() + 15 
    player.setx(move_right)
    if move_right > 285: #same boundary mechanics 
        player.setx(285)
    collision() #every time the player moves right it checks for the treasure 
    if player.ycor() == 88 and player.xcor() not in range(-75,90) or player.ycor() == 55 and player.xcor() not in range(-270,-120) or player.ycor() == 58 and player.xcor() not in range(120,270) or player.ycor() == -11 and player.xcor() not in range(-105,120) or player.ycor() == -44 and player.xcor() not in range(150,210) or player.ycor() == -47 and player.xcor() not in range(-210,-135) or player.ycor() == -83 and player.xcor() not in range(60,135) or player.ycor() == -86 and player.xcor() not in range (-120,-45) or player.ycor() == -140 and player.xcor() not in range (-35,35) or player.ycor() == -128 and player.xcor() not in range(-210,-140) or player.ycor() == - 131 and player.xcor() not in range (150,220) or player.ycor() == -182 and player.xcor() not in range(60,130) or player.ycor() == -233 and player.xcor() not in range(-35,35) or player.ycor() == -185 and player.xcor() not in range(-120,-50):
        while player.ycor() != -287:
            move_jump = player. ycor() - 3
            player.sety(move_jump)
            time.sleep(0) #this long code constantly checks if there is another platform under to land on rather than going straight through
            if player.ycor() == -287 or player.ycor() == -233 and player.xcor() in range (-35,35) or player.ycor() == -185 and player.xcor() in range (-120,-50) or player.ycor() == -182 and player.xcor() in range (60,130) or player.ycor() == - 131 and player.xcor() in range (150,220) or player.ycor() == - 128 and player.xcor() in range(-210,-140) or player.ycor() == -140 and player.xcor() in range(-35,35) or player.ycor() == - 86 and  player.xcor() in range(-120,-45) or player.ycor() == -83 and player.xcor() in range(60,135) or player.ycor() == -47 and player.xcor() in range(-210,-135) or player.ycor() == -44 and player.xcor() in range (150,210) or player.ycor() == -11 and player.xcor() in range(-120,120) or player.ycor() == 58 and player.xcor() in range(120,270) or player.ycor() == 55 and player.xcor() in range(-270,-120) or player.ycor() == 88 and player.xcor() in range(-75,90):
                break
    
    
def jump(): #this long line of code is all the coordinates of the platform and the ground, so if the cube is on the platforms or ground, then it can jump. Therefore preventing infinite jumping.
    if player.ycor() == -287 or player.ycor() == -233 and player.xcor() in range (-35,35) or player.ycor() == -185 and player.xcor() in range (-120,-50) or player.ycor() == -182 and player.xcor() in range (60,130) or player.ycor() == - 131 and player.xcor() in range (150,220) or player.ycor() == - 128 and player.xcor() in range(-210,-140) or player.ycor() == -140 and player.xcor() in range(-35,35) or player.ycor() == - 86 and  player.xcor() in range(-120,-45) or player.ycor() == -83 and player.xcor() in range(60,135) or player.ycor() == -47 and player.xcor() in range(-210,-135) or player.ycor() == -44 and player.xcor() in range (150,210) or player.ycor() == -11 and player.xcor() in range(-120,120) or player.ycor() == 58 and player.xcor() in range(120,270) or player.ycor() == 55 and player.xcor() in range(-270,-120) or player.ycor() == 88 and player.xcor() in range(-75,90):
        for loop in range(27): #I realized after that this is very ineffcient code since i could have just put all the coordinates for platform into a list rather than constantly repeating. 
            collision()
            move_jump = player.ycor() +3
            player.sety(move_jump)
            if player.ycor() == -233 and player.xcor() in range (-35,35) or player.ycor() == -185 and player.xcor() in range (-120,-50) or player.ycor() == -182 and player.xcor() in range (60,130) or player.ycor() == - 131 and player.xcor() in range (150,220) or player.ycor() == - 128 and player.xcor() in range(-210,-140) or player.ycor() == -140 and player.xcor() in range(-35,35) or player.ycor() == - 86 and  player.xcor() in range(-120,-45) or player.ycor() == -83 and player.xcor() in range(60,135) or player.ycor() == -47 and player.xcor() in range(-210,-135) or player.ycor() == -44 and player.xcor() in range (150,210) or player.ycor() == -11 and player.xcor() in range(-120,120) or player.ycor() == 58 and player.xcor() in range(120,270) or player.ycor() == 55 and player.xcor() in range(-270,-120) or player.ycor() == 88 and player.xcor() in range(-75,90):
                break
        while player.ycor() > -287: # keep on falling until it hits a platform or the ground(-287)
            if player.ycor() == -287 or player.ycor() == -233 and player.xcor() in range (-35,35) or player.ycor() == -185 and player.xcor() in range (-120,-50) or player.ycor() == -182 and player.xcor() in range (60,130) or player.ycor() == - 131 and player.xcor() in range (150,220) or player.ycor() == - 128 and player.xcor() in range(-210,-140) or player.ycor() == -140 and player.xcor() in range(-35,35) or player.ycor() == - 86 and  player.xcor() in range(-120,-45) or player.ycor() == -83 and player.xcor() in range(60,135) or player.ycor() == -47 and player.xcor() in range(-210,-135) or player.ycor() == -44 and player.xcor() in range (150,210) or player.ycor() == -11 and player.xcor() in range(-120,120) or player.ycor() == 58 and player.xcor() in range(120,270) or player.ycor() == 55 and player.xcor() in range(-270,-120) or player.ycor() == 88 and player.xcor() in range(-75,90):
                break
            collision()
            move_jump = player.ycor() - 3
            player.sety(move_jump)
            


#keybinding 
turtle.listen()
turtle.onkey(left,'Left')
turtle.onkey(right,'Right')
turtle.onkey(jump,'Up')

#movement of enemy
options = [1,2] #random choice 1 = left and 2 = right
def move_enemy4():
    direction = random.choices(options)
    if direction == [1]:
        move_lft4 = enemythree.xcor() - 15
        enemythree.setx(move_lft4)
    if direction == [2]:
        move_rt4 = enemythree.xcor() + 15
        enemythree.setx(move_rt4)
    
def move_enemy3():
    direction = random.choices(options)
    if direction == [1]:
        move_lft3 = en.xcor() - 15
        en.setx(move_lft3)
    if direction == [2]:
        move_rt3 = en.xcor() + 15
        en.setx(move_rt3)

def move_enemy2():
    direction = random.choices(options)
    if direction == [1]:
        move_lft2 = enemy2.xcor() - 15
        enemy2.setx(move_lft2)
    if direction == [2]:
        move_rt2 = enemy2.xcor() + 15
        enemy2.setx(move_rt2)

def move_enemy():
    direction = random.choices(options)
    if direction == [1]:
        move_lft = enemy.xcor() - 15
        enemy.setx(move_lft)
    if direction == [2]:
        move_rt = enemy.xcor() + 15
        enemy.setx(move_rt)
        
#endless loop for enemy movement and constantly checking if they have hit the player
while True:
    move_enemy()
    move_enemy2()
    move_enemy3()
    move_enemy4()
    collision_enemy()
    collision_enemy2()
    collision_enemy3()
    collision_enemy4()
    if enemy.xcor() == -270: #if statements used so the enemies won't float off their platforms 
        move_rt = enemy.xcor() + 15 #if they are at the edge of their platform then they will be sent back the opposite direction
        enemy.setx(move_rt)
    if enemy.xcor() == -135:
        move_lft = enemy.xcor() - 15
        enemy.setx(move_lft)
    if enemy2.xcor() == 135:
        move_rt2 = enemy2.xcor() + 15
        enemy2.setx(move_rt2)
    if enemy2.xcor() == 270:
        move_lft2 = enemy2.xcor() - 15
        enemy2.setx(move_lft2)
    if en.xcor() == -105:
        move_rt3 = en.xcor() + 15
        en.setx(move_rt3)
    if en.xcor() == 105:
        move_lft3 = en.xcor() - 15
        en.setx(move_lft3)
    if enemythree.xcor() == -105:
        move_rt4 = enemythree.xcor() + 15
        enemythree.setx(move_rt4)
    if enemythree.xcor() == 105:
        move_lft4 = enemythree.xcor() - 15
        enemythree.setx(move_lft4)        
