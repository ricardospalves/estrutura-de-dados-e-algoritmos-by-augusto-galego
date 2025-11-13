import heapq

class Solution:
  def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
    table = {}

    for t in times:
      if not table.get(t[0]):
        table[t[0]] = {
          t[1]: t[2]
        }
      else:
        table[t[0]][t[1]] = t[2]
    
    distances = {
      k: 0
    }

    min_heap = [
      (0, k)
    ]

    while min_heap:
      dist, node = heapq.heappop(min_heap)

      row = table.get(node)

      if row:
        for key, value in row.items():
          table_dist = distances.get(key, float('inf'))

          if dist + value < table_dist:
            distances[key] = dist + value

            heapq.heappush(min_heap, (dist + value, key))
    
    _max = -1

    if len(distances) < n:
      return _max
    
    for key, v in distances.items():
      _max = max(_max, v)
    
    if _max == 0:
      return -1
    
    return _max