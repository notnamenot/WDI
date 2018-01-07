class Node:
    def __init__(self,name):
        self.name=name
        self.next=None
            
    def __str__(self):
        return str(self.name)
    
class stos:
    def __init__(self):
        self.head=None
    
    def push(self,name):
        new=Node(name)
        if not self.head:
            self.head=new
        else:
            n=self.head
            while n.next:
                n=n.next
            n.next=new
            
    def pop(self):
        n = self.head
        self.head = self.head.next
        return n
        
    def show(self):
        n=self.head
        while n:
            print(n, end=' ')
            n=n.next


            
stos=stos()
stos.push("Iza")
stos.push("Zuzia")
print("<-show()")
print(stos.pop())
stos.show()
