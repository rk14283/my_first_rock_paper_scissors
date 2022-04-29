r = input("choose rock paper or scissors")

def rock(r): 
    if (r == "rock"):
        r = 0
        #print (r, "you choose rock")
    elif (r =="paper"):
        r = 1
        #print (r, "you choose paper")
    elif (r == "scissors"):
        r = 2
        #print (r, "you choose scissors")
    else:
        print ("choose rock, paper, or scissors")
    return r     
    


rock(r)
    


import random

n = random.randrange(0, 4)


def int_to_word_comp(n):
    if (n==0):
        print("computer choose rock")
    elif (n==1):
        print("computer choose paper")
    elif (n==2):
        print("computer choose scissors")    
    else:
        print("computer choose nothing")
    return n





def game(r,n):
    if r==0 and n==0:
        print("you choose rock\n it is a draw")
    elif r==1 and n==0:
        print("you choose paper\nyou win!!!")
    elif r==2 and n==0:
            print("you choose scissors\n you loose.")
            
    elif r==0 and n==1:
        print("you choose rock\n you loose.")
    elif r==1 and n==1:
        print("you choose paper\n it is a draw.")
    elif r==2 and n==1:
            print("you choose scissors\n you win!!!")
    elif r==0 and n==2:
        print("you choose rock\n you win!!!")
    elif r==1 and n==2:
        print("you choose paper\n you loose.")
    elif r==2 and n==2:
            print("you choose scissors\n it is a draw.")
    else:
        ("No output")
            
               
            
                  
game(rock(r),int_to_word_comp(n))        

    
