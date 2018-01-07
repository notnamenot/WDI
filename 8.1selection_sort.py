import random

n=int(input("Podaj zakres losowanej tablicy:\n"))

def tablica_losowych_liczb(n):
    tab=[]
    for i in range(n):
        tab.append(random.randint(0,n))
    return tab
    
tab=tablica_losowych_liczb(n)
print(tab)

def selection_sort(tab):
    for x in range(len(tab)-1):
        min=x                            #set the first unsorted element as the minimum
        for i in range(x,len(tab)):        #for each of the unsorted elements
            if(tab[i]<tab[min]):          #if element < currentMinimum
                min=i                      #set element as new minimum
        tab[min],tab[x]=tab[x],tab[min]   #swap minimum with first unsorted position
    return tab
    
print(selection_sort(tab))
