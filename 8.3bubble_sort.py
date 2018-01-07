import random

n=int(input("Podaj zakres losowanej tablicy:\n"))

def tablica_losowych_liczb(n):
    tab=[]
    for i in range(n):
        tab.append(random.randint(0,n))
    return tab
    
tab=tablica_losowych_liczb(n)
print(tab)

def bubble_sort(tab):
    for i in range(len(tab)-1):
        for k in range( len(tab)-1, i, -1 ):
            if (tab[k]<tab[k-1]):
                tab[k],tab[k-1]=tab[k-1],tab[k]
    return tab        
              
print(bubble_sort(tab))
