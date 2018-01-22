class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)
        
class Stos:
    def __init__(self):
        self.head = None
    
    def push(self,data):
        new = Node(data)
        if not self.head:
            self.head = new
        else:
            new.next = self.head
            self.head = new
        
    def pop(self):
        n = self.head
        self.head = self.head.next
        return n.data
        
wyr=input()
tmp=''
stos = Stos()

for i in range(len(wyr)):
    if wyr[i].isdigit():
        tmp+=wyr[i]
    
    if wyr[i]==' ' and len(tmp)>0:
        stos.push(int(tmp))
        tmp=''
        
    if wyr[i]=='+':
        a = stos.pop()
        b = stos.pop()   
        stos.push(b+a)
    
    if wyr[i]=='-':
        a = stos.pop()
        b = stos.pop()   
        stos.push(b-a)
    
    if wyr[i]=='*':
        a = stos.pop()
        b = stos.pop()   
        stos.push(b*a)
    
    if wyr[i]=='/':
        a = stos.pop()
        b = stos.pop()   
        stos.push(b/a)
    
print(stos.pop())
