#pół choinki

n=int(input("Podaj liczbę n\n"))
if n<2:
    print("n musi byc wieksze niz 2")
    n=int(input("Podaj liczbę n\n"))        #długiść ostatniej lini

for i in range(2, n+1):
    for j in range(1, i+1):
        print("x"*j)
        
#cała choinka 

n=int(input("Podaj liczbę n\n"))         #ostatnia linia zawiera 2n +1 znaków
if n<1:
    print("n musi byc wieksze niz 1")
    n=int(input("Podaj liczbę n\n"))

for i in range(0, n):
    for i in range(0, (n-1)+i):
        print(" "*(2*n-i)+"x"*2*i+"x")

        
# program rysuje choinke o podstawie 2k+1
n=int(input("Podaj liczbe n>=1"))
for i in range (1,n+1):
    for k in range (0,i+1):
        print(" "*(n-k+1),end="")
        print("x"*(2*k+1))
            
