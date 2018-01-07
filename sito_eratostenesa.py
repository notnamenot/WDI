import math

def tablica_liczb(n):
    tablica=[]
    for i in range(1,n+1):
        tablica.append(i)
    return tablica
    
def sito(n):
    liczba=1
    tab=tablica_liczb(n)
    while True:
        if liczba>int(math.sqrt(n)):   #warunek zakonczenia działania algorytmu
            return tab
        for i in tab:
            if( not(i%liczba) and not(liczba==i) and liczba!=1):      #usuń element jesli jest podzielny przez obeczną liczbę
                tab.remove(i)
        i=tab.index(liczba)+1
        liczba=tab[i]
        
n=int(input("Podaj górny zakres sita:\n")
pierwsze=sito(n)
for pierwsza in pierwsze:
    print(pierwsza)
        
        

      
  
