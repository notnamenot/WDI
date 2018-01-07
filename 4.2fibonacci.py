import time

n=int(input("Podaj n-ty wyraz ciągu:\n"))

def fib_it(n):
    a,b=0,1
    for i in range(n):
        a,b=b,a+b
    return a
    
def fib_rek(n):
    if n==0: 
        return 0
    elif n==1: 
        return 1
    else:
        fib=fib_rek(n-1)+fib_rek(n-2)
    return fib



t0=time.clock()
print(fib_it(n))   
print("Czas iteracyjnie:")
print(time.clock()-t0)
t0=time.clock()
print(fib_rek(n))   
print("Czas rekurencyjnie:")
print(time.clock()-t0)
