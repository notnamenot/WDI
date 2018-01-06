#pół choinki

n=int(input("Podaj liczbę n\n"))
if n<2:
    print("n musi byc wieksze niz 2")
    n=int(input("Podaj liczbę n\n"))        #długiść ostatniej lini

for i in range(2, n+1):
    for j in range(1, i+1):
        print("x"*j)
        
