xCoordinateOfBall = 100 
yCoordinateOfBall = 300
xspeed = 20
yspeed = 12
def setup():
    size(400,400)
    background(0,0,0)
    
def draw():
   global xCoordinateOfBall,yCoordinateOfBall, xspeed,yspeed 
   global randrange
   ellipse(xCoordinateOfBall,yCoordinateOfBall,40,40)
   xCoordinateOfBall += xspeed
   yCoordinateOfBall += yspeed
   if xCoordinateOfBall > 400 or xCoordinateOfBall < 10:
      xspeed *= -1
   if yCoordinateOfBall > 400 or yCoordinateOfBall < 10:
       yspeed *=  -1
   rect(1,1,1,1)
       

   

   

    
        