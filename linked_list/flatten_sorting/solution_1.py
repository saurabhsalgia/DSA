
class Node:
    def __init__(self, data, next=None, down=None):
        self.data = data
        self.next = next
        self.down = down
  
    def __str__(self):
        return f'{self.data}-->{self.next}'

    def flatten(self):
        orig = self
        while self.next is not None:
            next_node = self.next
            print('ne', next_node)
            self.next = self.down
            self = next_node
        else:
            self.next = self.down
            # print(self)
        print(self)
                

n1=Node(5)
n2=Node(10)
n3=Node(19)
n4=Node(28)
n1.next = n2
n2.next = n3
n3.next = n4

n5=Node(7)
n6=Node(8)
n7=Node(30)
n1.down = n5
n5.down = n6
n6.down = n7

n8=Node(20)
n2.down = n8

n9=Node(22)
n10=Node(50)
n3.down = n9
n9.down = n10

n11=Node(35)
n12=Node(40)
n13=Node(45)
n4.down = n11
n11.down = n12
n12.down = n13

n1.flatten()


