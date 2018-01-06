def dec_to_bin(d):
    b=''
    while d>0:
        b+=str(d%2)
        d//=2
    b=b[::-1]
    return b
    
d=int(input("Podaj liczbę w systemie dziesiętnym:\n"))
print("Ta liczba w systemie binarnym wynosi", dec_to_bin(d))
