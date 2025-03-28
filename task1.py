# 9. Linked List Implementation
# ✅ Task: Implement a simple Singly Linked List in Python.
#  🔹 Requirements:
# Add methods for inserting, deleting, and displaying nodes.


# python
# CopyEdit

class Node:
    def __init__(self, data):
        self.data1 = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
      newnode = Node(data)
      if not self.head:
          self.head = newnode
          return
      temp = self.head
      while temp.next:
          temp=temp.next
      temp.next = newnode     
 
    def delete(self, key):
        temp = self.head

        if temp and temp.data1 == key:
            self.head = temp.next
            temp = None
            return
        prev = None
        while temp and temp.data1 != key:
            prev = temptemp = temp.next
        if not temp:
            print(f"value {key} not found in ")
            return
        prev.next = temp.nexttemp =None
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ->")
            temp = temp.next
        print()

# Example usage
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.display()