# Definition for singly-linked list.
# class ListNode(object):
#   def __init__(self, x):
#     self.val = x
#     self.next = None

class Solution(object):
  def hasCycle(self, head):
    """
    :type head: ListNode
    :rtype: bool
    """
    slow_pointer = head
    fast_pointer = head

    while fast_pointer and fast_pointer.next:
      slow_pointer = slow_pointer.next
      fast_pointer = fast_pointer.next.next

      if fast_pointer == slow_pointer:
        return True
    
    return False