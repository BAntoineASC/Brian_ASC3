from random import *
xCoordinateOfBall = 100 
yCoordinateOfBall = 300
xspeed = 0
yspeed = 2
def setup():
    size(400,400)
    
    
def draw():
   global xCoordinateOfBall,yCoordinateOfBall, xspeed,yspeed 
   global randrange
   background(255)
   fill(randrange(255))
   ellipse(xCoordinateOfBall,yCoordinateOfBall,40,40)
   stroke(3)
   xCoordinateOfBall += xspeed
   yCoordinateOfBall += yspeed
   if xCoordinateOfBall > 400 or xCoordinateOfBall < 10:
      xspeed *= -1
   if yCoordinateOfBall > 400 or yCoordinateOfBall < 10:
       yspeed *=  -1
   rect(mouseX,380,40,10)
   if xCoordinateOfBall > mouseX - 190 and xCoordinateOfBall < xCoordinateOfBall and mouseX + 190 and yCoordinateOfBall < 400:
       yspeed *= -1


   #constant 
   #conditional
   
   # 2 < x < 4