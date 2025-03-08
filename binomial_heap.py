class BinomialNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.sibling = None

    def link(self, other):
        """
        Link the other node as a child of self.
        Assumes that self.key <= other.key.
        """
        other.parent = self
        other.sibling = self.child
        self.child = other
        self.degree += 1


class BinomialHeap:
    def __init__(self):
        self.head = None  # Root list of binomial trees

    def merge_roots(self, h):
        """
        Merge two root lists sorted by tree degree.
        """
        new_head = None
        tail = None
        a = self.head
        b = h.head
        if a is None:
            return b
        if b is None:
            return a

        if a.degree <= b.degree:
            new_head = a
            a = a.sibling
        else:
            new_head = b
            b = b.sibling
        tail = new_head

        while a and b:
            if a.degree <= b.degree:
                tail.sibling = a
                a = a.sibling
            else:
                tail.sibling = b
                b = b.sibling
            tail = tail.sibling

        tail.sibling = a if a else b
        return new_head

    def union(self, other):
        """
        Merge two binomial heaps.
        """
        new_heap = BinomialHeap()
        new_heap.head = self.merge_roots(other)
        if new_heap.head is None:
            return new_heap

        prev = None
        curr = new_heap.head
        next = curr.sibling
        while next:
            # If the degrees are different or if three consecutive trees have the same degree, do not merge
            if (curr.degree != next.degree) or (next.sibling and next.sibling.degree == curr.degree):
                prev = curr
                curr = next
            else:
                if curr.key <= next.key:
                    curr.sibling = next.sibling
                    curr.link(next)
                else:
                    if prev is None:
                        new_heap.head = next
                    else:
                        prev.sibling = next
                    next.link(curr)
                    curr = next
            next = curr.sibling
        return new_heap

    def insert(self, key):
        """
        Insert a new element by creating a single-node heap and merging it with the current heap.
        """
        new_node = BinomialNode(key)
        new_heap = BinomialHeap()
        new_heap.head = new_node
        unioned = self.union(new_heap)
        self.head = unioned.head
        return new_node

    def find_min(self):
        """
        Return the node with the minimum key (without removing it).
        """
        if self.head is None:
            return None
        y = None
        x = self.head
        min_key = float('inf')
        while x:
            if x.key < min_key:
                min_key = x.key
                y = x
            x = x.sibling
        return y

    def delete_min(self):
        """
        Remove the minimum element from the heap and return its key.
        Process:
          1. Find the minimum node in the root list.
          2. Remove the tree containing the minimum node.
          3. Reverse the order of its children.
          4. Merge the children with the remaining heap.
        """
        if self.head is None:
            return None

        # Find the minimum node and its previous node in the root list
        min_prev = None
        min_node = self.head
        prev = None
        curr = self.head
        while curr:
            if curr.key < min_node.key:
                min_node = curr
                min_prev = prev
            prev = curr
            curr = curr.sibling

        # Remove the min_node from the root list
        if min_prev:
            min_prev.sibling = min_node.sibling
        else:
            self.head = min_node.sibling

        # Reverse the order of min_node's children
        child = min_node.child
        new_head = None
        while child:
            next_child = child.sibling
            child.sibling = new_head
            child.parent = None
            new_head = child
            child = next_child

        # Merge the reversed child list with the current heap
        temp_heap = BinomialHeap()
        temp_heap.head = new_head
        new_heap = self.union(temp_heap)
        self.head = new_heap.head

        return min_node.key
