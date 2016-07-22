from random import *
x = 0
y = 1

bullet = False
bulletPush = 10
spaceMover = 350 #moves spaceship
c=0 # coordinate of Y
dirX = 10
bulletY = 550
def setup():
    size(600,600)
    
def draw():
    global x 
    global y
    background(0,0,0)
    global dirX, dirY, c,b, bullet, bulletY

    #fill(255,25,25)
    #rect(dirx + 125,diry + 200,100,100)
 #v          -- ----- ------ where to make squares -------------------
    #                                   down here      
    fill(124,5,5)
    rect(x + 100,y + 100,50,50)
    
    fill(124,5,5)
    rect(x + 200,y +100,50,50)

    fill(124,5,5)
    rect(x + 300,y +100,50,50)

    fill(124,5,5)
    rect(x,y +100,50,50) # this is the first box :)
    
    fill(0,0,255);
    rect(spaceMover, 550, 58, 20)
    rect(spaceMover+20,530,20,20)
    fill(0,255,255)
    ellipse(56,46,60,60)
    
    if x == 200:  #smaller the faster it stops to the right
        y = 0
    if x <10:     #larger, the faster it stops from the right
        y =50
        
    if y == 0:
        x =x-1
    else:
        x =x + 1
    if y == 400:
        x = x +50

    if bullet == True:
        global randrange
        fill(255,0,0)
        rect(spaceMover+20,bulletY,10,10)
        bulletY = bulletY -5
    if bulletY < 0:
       bullet = False
       bulletY = 550
    
def keyPressed():
    global bulletY, bullet
    global spaceMover,c
    dirX = 10
    dirY = 0
    #if (key == CODED):
    print("Key pressed keycode : ",keyCode) 
    if (keyCode == 39) and spaceMover < 550:   
        spaceMover = spaceMover + dirX
    if (keyCode == 37)and spaceMover > 0:  
        spaceMover = spaceMover - dirX
    if (keyCode == 32):
        bullet = True
                           
        #-bulletPush 
    
    
   