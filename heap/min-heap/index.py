class MinHeap:
  def __init__(self) -> None:
    self.heap = []
  
  def _left_child(self, index):
    return ((index * 2) + 1)
  
  def _right_child(self, index):
    return ((index * 2) + 2)
  
  def _parent(self, index):
    return (index - 1) // 2
  
  def _heapfy_up(self, index):
    if index == 0:
      return
    
    parent_index = self._parent(index)

    if self.heap[index] < self.heap[parent_index]:
      self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
      self._heapfy_up(parent_index)
  
  def _heapfy_down(self, index):
    size = len(self.heap)
    left = self._left_child(index)
    right = self._right_child(index)
    smallest = index

    if (left < size) and (self.heap[left] < self.heap[smallest]):
      smallest = left
    
    if (right < size) and (self.heap[right] < self.heap[smallest]):
      smallest = right
    
    if smallest == index:
      return
    
    self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
    self._heapfy_down(smallest)
  
  def insert(self, value):
    self.heap.append(value)
    self._heapfy_up(len(self.heap) - 1)
  
  def pop_min(self):
    heap_length = len(self.heap)

    if heap_length == 0:
      raise IndexError("Heap is empty.")
    
    if heap_length == 1:
      return self.heap.pop()
    
    root = self.heap[0]

    self.heap[0] = self.heap.pop()

    self._heapfy_down(0)

    return root

min_heap = MinHeap()

min_heap.insert(0)
min_heap.insert(1)
min_heap.insert(2)
min_heap.insert(3)
min_heap.insert(4)
min_heap.insert(5)
min_heap.insert(0)
min_heap.insert(0)

print(min_heap.pop_min())
print(min_heap.heap)