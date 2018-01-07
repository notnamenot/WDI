def dec_to_bin(d):
    b=''
    while d>0:
        b+=str(d%2)
        d//=2
    b=b[::-1]
    return b
    
d=int(input("Podaj liczbę w systemie dziesiętnym:\n"))
print("Ta liczba w systemie binarnym wynosi", dec_to_bin(d))



def dec_to_random(d,sys):     #decimal, system
    r=""
    
    while d>0:
        r+=str(d%sys)
        d//=sys
    r=r[::-1]
    return r        #str

d=int(input("Podaj liczbę w systemie dziesiątkowycm:\n"))   #int
sys=int(input("Podaj na jaki system przeliczać:\n"))        #int

print("Liczba w nowym systemie wynosi:\n", dec_to_random(d,sys))

