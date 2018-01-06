
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
