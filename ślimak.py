def ile(h,x,y,z):
    wynik=0
    wys=0
    while wys<h:
        if wys%z==0:
            wys+=x
        else:
            wys+=(x-y)
        wynik+=1
    return wynik
    
    
h=int(input("podaj wysokosc "))
x=int(input("podaj x "))
y=int(input("podaj y "))
z=int(input("podaj z "))
ile=ile(h,x,y,z)
print(ile)
