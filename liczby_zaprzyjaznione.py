Liczby zaprzyjaźnione to para różnych liczb naturalnych, takich że suma dzielników każdej z tych liczb równa się drugiej

    220 = 1 + 2 + 4 + 71 + 142 (dzielniki 284)
    284 = 1 + 2 + 4 + 5 + 10 + 11 + 20 + 22 + 44 + 55 + 110 (dzielniki 220)
    
    
def suma(a):
    suma=0
    for i in range(1,a//2+1):
        if a%i==0:
            suma+=i
    return suma

n=int(input("zakres(duży)"))
    
for i in range(1,n+1):
    d=suma(i)
    if suma(d)==i and suma(i)==d and i!=d:
        print(i,d)

