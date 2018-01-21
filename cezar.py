text=input("Podaj tekst do zaszyfrowania:\n")
p=int(input("Podaj przesuniece:\n"))

def zamiana(text):
    text.lower()
    text.replace(" ","")
    return text

#tekst=zamiana(text)



def cezar(tekst,p):
    szyfr=[]
    for i in range(len(tekst)):
        for j in range(26):
            if tekst[i]==chr(97+j):
                szyfr.append(chr(97+(j+p)%26))
    wynik="".join(szyfr)
    return wynik

#szyfr=cezar(tekst,p)

def de_cezar(szyfr,p):
    rozw=[]
    for i in range(len(szyfr)):
        for j in range(26):
            if szyfr[i]==chr(97+j):
                rozw.append(chr(97+(j-p)%26))
    w="".join(rozw)
    return w
    

print("Zaszyfrowany tekst:\n", cezar(zamiana(text),p))
print("Rozszyfrowany tekst:\n", de_cezar(cezar(zamiana(text),p),p))
