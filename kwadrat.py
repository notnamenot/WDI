import time
def odleglosc (x_p,x_s,y_p,y_s):
    return max(abs(x_p-x_s),abs(y_p-y_s))    
    
x=int(input("Podaj szerokosc planszy "))
y=int(input("Podaj wysokosc planszy "))
a=x//2
b=y//2
z=min(x,y)

for n in range (1,-2,-2):
    for i in range (int((-z//2*n)/2+(z//2)/2),int(n*(z//2 + 1)/2+(z//2 - 1)/2),n):
        for j in range (0,y):
            for k in range (0,x):
                if odleglosc (k,a,j,b)==i and odleglosc (k,a,j,b)<=z//2:
                    print ("X",end="")
                else:
                    print ("O",end="")
            print()
        print()
        time.sleep(1)
