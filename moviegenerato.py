from random import * 
def main():
    sList = ["The ancient","uprising","The journey","The lost tales of","The amazing","The", "Return of the","The trials and tribulations of the","The rise of","The beginning"] 
    adjectiveList = [ "brave" , "amused" , "delightful" , "grateful" , "lively" , "thankful" , "victorious" , "relieved" , "energetic" , "thrilled" ]
    ballList = ["Kyrie","Curry","Lebron","durant","Duncan","Kobe","Melo","Drose","Cp3","Harden"]
    print(sList[randrange(len(sList))] + adjectiveList[randrange(len(adjectiveList))] +
    ballList[randrange(len(ballList))])
main()