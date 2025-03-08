class BinaryHeap:
    def __init__(self):
        self.heap = []

    def insert(self, key):
        """Insert a new element while maintaining the heap property."""
        self.heap.append(key)
        self._bubble_up(len(self.heap) - 1)

    def _bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index] < self.heap[parent]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                index = parent
            else:
                break

    def delete_min(self):
        """Remove and return the minimum element from the heap."""
        if not self.heap:
            return None
        min_elem = self.heap[0]
        last_elem = self.heap.pop()
        if self.heap:
            self.heap[0] = last_elem
            self._bubble_down(0)
        return min_elem

    def _bubble_down(self, index):
        n = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break
