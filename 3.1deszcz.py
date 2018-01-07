import time
import random
#random.seed()

length=int(input("Podaj długość planszy "))
height=int(input("Podaj wysokość planszy "))
deszcz=[-1]*height
for k in range(height):
    rand=random.randint(0,length-1)
    deszcz.insert(0,rand)           #od której linijki zaczyna wstawiać *
    deszcz.pop()                    # removes and returns  last object
    for i in range(height):
        for j in range(length):
            if deszcz[i]==j:
                print ("*",end="")
            else:
                print ("O",end="")
        print()
    print()
    time.sleep(0.3)
