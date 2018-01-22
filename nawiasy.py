class Node:
    def __init__(self,char):
        self.char = char
        self.next = None
        
    def __str__(self):
        return str(self.char)
    
class stos:
    def __init__(self):
        self.head = None
    
    def push(self,char):
        new = Node(char)
        if not self.head:
            self.head = new
        else:
            new.next = self.head
            self.head = new
        
    def pop(self):
        n = self.head
        self.head = self.head.next
        return n.char
        
    def isEmpty(self):
        if not self.head:
            return True
        else:
            return False
            
wyr = input("Podaj wyrazenie ")
stos = stos()
for i in range (len(wyr)):
    if wyr[i]=='(' or wyr[i]=='[' or wyr[i]=='{':
        stos.push(wyr[i])
    
    if wyr[i]==')' and not stos.isEmpty():
        if stos.pop()!='(':
            print("Bledne wyrazenie")
            break
           
    if wyr[i]==']' and not stos.isEmpty():
        if stos.pop()!='[':
            print("Bledne wyrazenie")
            break
        
    if wyr[i]=='}' and not stos.isEmpty():
         if stos.pop()!='{':
            print("Bledne wyrazenie")
            break

if stos.isEmpty():
    print("Poprawne wyrazenie")
else:
    print("Bledne wyrazenie")
