def sys_to_dec(b,sys):
    d=0
    for i in range(len(b)):
        if ord(b[i])>=48 and ord(b[i])<=57:
            d+=(sys**(len(b)-i-1))*(ord(b[i])-48)
        elif ord(b[i])>=65:
            d+=(sys**(len(b)-i-1))*(ord(b[i])-55)
    return d

def dec_to_sys(dec,sys1):
    r=""
    while dec>0:
        if dec%sys1>=0 and dec%sys1<=9:
            r+=str(dec%sys1)
        elif dec%sys1>9:
            r+=chr(dec%sys1+55)
        dec//=sys1
    r=r[::-1]
    return r
        



b=input("Podaj liczbę do konwersji:\n")
sys=int(input("Podaj system z konwersji:\n"))

dec=sys_to_dec(b,sys)
#print("Liczba w dziesietnym:\n", dec)

sys1=int(input("System na konwersje:\n"))
s=dec_to_sys(dec, sys1)

print("Liczba w nowym systemie:\n", s)    






"""
l=input("Podaj liczbę do konwersji:\n")    
sys=int(input("Podaj system z konwersji:\n"))
sys1=int(input("Podaj system do konwersji:\n"))     

def sys_to_dec(l,sys):
    dec=0
    for i in range(len(l)):
        dec+=sys**(len(l)-i-1)*int(l[i])
    return dec
#print(sys_to_dec(l,sys))


def dec_to_sys(a,sys1):
    dec=sys_to_dec(l,sys)
    r=""
    while dec>0:
        r+=str(dec%sys1)
        dec//=sys1
    r=r[::-1]    
    return r
          
print("Liczba po konwersji to:", dec_to_sys(sys_to_dec(l,sys) ,sys1))
"""
