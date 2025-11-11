import math

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node 

    def insert_gcd(self):
        curr = self.head
        while curr and curr.next:
            gcd_val = math.gcd(curr.data, curr.next.data)
            gcd_node = Node(gcd_val)
            gcd_node.next = curr.next
            curr.next = gcd_node
            curr = gcd_node.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")      

arr = list(map(int, input().split()))

ll = LinkedList()
for num in arr:
    ll.append(num)

print("\nOriginal list:")
ll.display()

ll.insert_gcd()

print("\nModified list with GCDs inserted:")
ll.display()



