from random import randint
board = []
turn=0
for x in range(5):
    board.append(["0"]*5)
board[randint(0,len(board)-1)][randint(0,len(board[0])-1)]="ship"
#print(board) 

'''for i in range(5):
    print(board[i])'''

def setup():
    size(500,500)
                       
def print_board(board):
    background(255,255,255)
    x =0
    for k in board:
        y=0
        for i in k:
            if i=="0" or i=="ship":
                fill(0,0,255)
                rect(x,y,100,100)
            else:
                fill(255,0,0)
                ellipse(x,y,100,100)
            y = y + 100
        x = x +100

        
def mousePressed():
    global turn 
    if turn <5:
         turn += 1
         mX= int(mouseX/100)
         mY= int(mouseY/100)
         if board[mX][mY] == "ship":
            print("you sunk my battleship")
            background(0,255,0)
            textSize(50)
            #text("YOU WIN!!!!!!",100,250)
         elif board[mX][mY] == "X":
             print("you already guessed that ... now you lose a turn")
         elif board[mX][mY] == "0":
             print("you missed! Try Again!")
             board[mX][mY] ="X"
             print_board(board)
         if turn > 4:
            background(255,255,255)
            textSize(50)
            text("GameOver!!",50,250)

def draw():
    global board, turn
    
    if turn < 5:
        print_board(board)
             
    '''for k in range(5):
        rect(0,y,100,100)
        y = y +100
        '''

                
    '''background(255,0,0)
    x=0
    for row in board:
        y=0
       ''' 