class Node:
  def __init__(self, value=0,next=None):
    self.value = value
    self.next = next

node_7 = Node(7)
node_1 = Node(1, next=node_7)
node_3 = Node(3, next=node_1)
node_9 = Node(9, next=node_3)

def find_middle(head):
  slow_pointer = head
  fast_pointer = head.next

  while fast_pointer and fast_pointer.next:
    slow_pointer = slow_pointer.next
    fast_pointer = fast_pointer.next.next
  
  return slow_pointer

def merge(list_1, list_2):
  head = Node()
  tail = head

  while list_1 and list_2:
    if list_1.value < list_2.value:
      tail.next = list_1
      list_1 = list_1.next
    else:
      tail.next = list_2
      list_2 = list_2.next
    
    tail = tail.next
  
  tail.next = list_1 or list_2

  return head.next

def mergesort(head):
  if not head or not head.next:
    return head

  middle = find_middle(head)
  after_middle = middle.next

  middle.next = None

  left_list = mergesort(head)
  right_list = mergesort(after_middle)
  sorted_list = merge(left_list, right_list)

  return sorted_list

my_list = mergesort(node_9)

print(my_list)