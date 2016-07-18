from random import *
def setup():
    size(400,400)
    

def draw(): 
    rect(mouseX,mouseY,10,10)
    strokeWeight(10)
    stroke(randrange(255),10,15)
    triangle(mouseX,mouseY, 58, 20, 86, 75);
    quad(mouseX, mouseY, 86, 20, 69, 63, 30, 76);
    
def mousePressed():
     ellipse(mouseX, mouseY, 30, 150)
     rect(30, 20, 55, 55)
     