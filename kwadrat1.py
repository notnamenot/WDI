import time

x = int(input("Podaj szerokość "))
y = int(input("Podaj wysokość "))
a = min(x,y)

for i in range(a//2+1):
    for j in range(i):
        print("X"*x)
    for j in range(y-2*i):
        print("X"*i+"O"*(x-2*i)+"X"*i)
    for j in range(i):
        print("X"*x)
    time.sleep(0.3)
    print()

for i in range(a//2+1):
    for j in range(i):
        print("O"*x)
    for j in range(y-2*i):
        print("O"*i+"X"*(x-2*i)+"O"*i)
    for j in range(i):
        print("O"*x)
    time.sleep(0.3)
    print() 

for i in range(y):
    print("O"*x)
