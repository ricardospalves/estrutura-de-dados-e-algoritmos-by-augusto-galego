class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
      heap = []

      def push_node(heap, node):
        if node:
          heapq.heappush(heap, (node.val, id(node), node))

      for node in lists:
        push_node(heap, node)

      dummy = ListNode()
      current = dummy

      while heap:
        _, _, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        if node.next:
          push_node(heap, node.next)

      return dummy.next