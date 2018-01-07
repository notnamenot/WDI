import time

def silnia_it(n):
    silnia = 1
    for i in range(1,n+1):
        silnia *= i
    return silnia
    
def silnia_rek(n):
    if n==0 or n==1 :
        return 1
    else:
        silnia = silnia_rek(n-1)*n
    return silnia
    
n=int(input("Podeaj liczbę:\n")
t0=time.clock()
print(silnia_it(n))
print("Czas wykonania iteracji:", time.clock()-t0)
t0=time.clock()
print(silnia_rek(n))
print("Czas wykonania rekurencji:", time.clock()-t0)
