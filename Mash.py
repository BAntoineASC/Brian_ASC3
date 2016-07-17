from random import *
user_input = []
get_input = raw_input("You ready to play MASH or nah?") 
user_input.append(get_input)
print(user_input)
def mash():

    a=raw_input("Who do you want to marry?")
    b=raw_input("Who do you want to marry?")
    c=raw_input("Who do you want to marry?")
    sList = [a,c,b,"Beyonce"]
    e=raw_input("where do you want to live?") 
    f=raw_input("where do you want to live?")
    adjectiveList = [e , f , "a bus stop"]
    ballList = ["10","1","4","5","6","7","2","9"]
    #user_input = []
    get_input = raw_input("Who do you want to marry?") 
    user_input.append(sList)
    user_input = []
    get_input = raw_input("where do you want to live?") 
    user_input.append(adjectiveList)
    user_input = []
    get_input = raw_input("how many kids?") 
    user_input.append(ballList)
    print(sList[randrange(len(sList))] + adjectiveList[randrange(len(adjectiveList))] +
    ballList[randrange(len(ballList))])
mash()
