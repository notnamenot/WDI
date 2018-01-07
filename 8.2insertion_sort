import random

n=int(input("Podaj zakres losowanej tablicy:\n"))

def tablica_losowych_liczb(n):
    tab=[]
    for i in range(n):
        tab.append(random.randint(0,n))
    return tab
    
tab=tablica_losowych_liczb(n)
print(tab)

def insertion_sort(tab):               
    for i in range(1,len(tab)):           
        x=tab[i]                      
        j=i-1                        
        while (j>=0 and tab[j]>x): 
            tab[j+1]=tab[j]             
            j-=1    
        tab[j+1]=x         
    return tab
    
print(insertion_sort(tab))
