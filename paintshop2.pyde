def setup():
    size(400,400)
    background(255,255,255)
pick_color = color(0,0,0) 
   
def draw():
    
    fill(255,255,0)
    rect(0,0,50,50)
    fill(0,255,0)
    rect(50,0,50,50)
    fill(212,175,55)        
    rect(100,0,50,50)
    fill(0,230,255)
    rect(150,0,50,50)
    fill(255,102,178)
    rect(200,0,50,50)
    fill(0,102,204)
    rect(250,0,50,50)
    fill(0,0,0)
    rect(300,0,50,50)
    fill(153,0,76)
    rect(350,0,50,50)
    fill(255,255,255)
    rect(350,50,50,50)
    global pick_color

    if mouseButton == LEFT:
          if mouseY < 50 and mouseX < 50:
                pick_color = 1
          elif mouseY < 50 and mouseX > 50 and mouseX < 100:
                 pick_color = 2 
          elif mouseY < 50 and mouseX > 100 and mouseX < 150:
                 pick_color = 3
          elif mouseY < 50 and mouseX > 150 and mouseX < 200:
                 pick_color = 4
          elif mouseY < 50 and mouseX > 200 and mouseX < 250:
                 pick_color = 5
          elif mouseY < 50 and mouseX > 250 and mouseX < 300:
                 pick_color = 6
          elif mouseY < 50 and mouseX > 300 and mouseX < 350:
                 pick_color = 7
          elif mouseY < 50 and mouseX > 350 and mouseX < 400:
                 pick_color = 8
          else:
                if pick_color == 1:
                    noStroke()
                    fill(255,255,0)
                    ellipse(mouseX,mouseY,50,50)
                if pick_color == 2:
                    noStroke()
                    fill(0,255,0)
                    ellipse(mouseX,mouseY,50,50)
                if pick_color == 3:
                    noStroke()
                    fill(212,175,55) 
                    ellipse(mouseX,mouseY,50,50)
                if pick_color == 4:
                    noStroke()
                    fill(0,230,255)
                    ellipse(mouseX,mouseY,50,50)
                if pick_color == 5:
                    noStroke()
                    fill(255,102,178)
                    ellipse(mouseX,mouseY,50,50)
                if pick_color == 6:
                    noStroke()
                    fill(0,102,204)
                    ellipse(mouseX,mouseY,50,50)
                if pick_color == 7:
                    noStroke()
                    fill(0,0,0)
                    ellipse(mouseX,mouseY,50,50)
                if pick_color == 8:
                    noStroke()
                    fill(153,0,76)
                    ellipse(mouseX,mouseY,50,50)
    
                
             
            