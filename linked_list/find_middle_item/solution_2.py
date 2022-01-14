class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
      
    def __str__(self):
        return f'{self.data}-->{self.next}'
     
    def get_middle(self):
        slow = self
        fast = self
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow.data
           
        
            
        
n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
# n6=Node(6)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
# n5.next = n6
print(n1.get_middle())
