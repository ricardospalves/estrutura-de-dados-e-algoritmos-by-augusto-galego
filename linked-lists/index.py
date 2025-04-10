class Node:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.previous = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  def add_to_head(self, value):
    new_node = Node(value)
    new_node.next = self.head

    if self.head:
      self.head.previous = new_node
    else:
      self.tail = new_node
    
    self.head = new_node
  
  def add_to_tail(self, value):
    new_node = Node(value)
    new_node.previous = self.tail

    if self.tail:
      self.tail.next = new_node
    else:
      self.head = new_node
    
    self.tail = new_node
  
  def delete_from_head(self):
    if not self.head:
      return None

    removed_value = self.head.value
    self.head = self.head.next

    if self.head:
      self.head.previous = None
    else:
      self.tail = None

    return removed_value
  
  def delete_from_tail(self):
    if not self.tail:
      return None

    removed_value = self.tail.value
    self.tail = self.tail.previous

    if self.tail:
      self.tail.previous = None
    else:
      self.head = None

    return removed_value

dll = DoublyLinkedList()

dll.add_to_head(3)
dll.add_to_head(2)
dll.add_to_head(1)
dll.add_to_tail(4)
dll.add_to_tail(5)

# Forward: [1, 2, 3, 4, 5]
# Backward: [5, 4, 3, 2, 1]

print(dll.delete_from_head()) # Removes 1
print(dll.delete_from_tail()) # Removes 5
print(dll.delete_from_head()) # Removes 2
print(dll.delete_from_tail()) # Removes 4