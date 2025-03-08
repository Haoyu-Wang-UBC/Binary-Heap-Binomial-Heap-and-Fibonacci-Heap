import math

class FibonacciNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        # Circular doubly-linked list: initially, the node points to itself.
        self.left = self
        self.right = self
        self.mark = False

class FibonacciHeap:
    def __init__(self):
        self.min = None   # Pointer to the minimum node in the root list.
        self.n = 0        # Total number of nodes in the heap.

    def insert(self, key):
        """
        Insert a new node into the Fibonacci heap.
        """
        node = FibonacciNode(key)
        if self.min is None:
            self.min = node
        else:
            # Insert node into the root list (adjacent to min)
            node.left = self.min
            node.right = self.min.right
            self.min.right.left = node
            self.min.right = node
            if node.key < self.min.key:
                self.min = node
        self.n += 1
        return node

    def delete_min(self):
        """
        Remove the minimum node from the heap and return its key.
        """
        z = self.min
        if z is not None:
            # Add all of z's children to the root list.
            if z.child is not None:
                # Collect all children of z.
                children = []
                x = z.child
                while True:
                    children.append(x)
                    x = x.right
                    if x == z.child:
                        break
                for x in children:
                    # Remove x from the child list.
                    x.left.right = x.right
                    x.right.left = x.left
                    # Add x to the root list.
                    x.left = self.min
                    x.right = self.min.right
                    self.min.right.left = x
                    self.min.right = x
                    x.parent = None
            # Remove z from the root list.
            z.left.right = z.right
            z.right.left = z.left
            if z == z.right:
                self.min = None
            else:
                self.min = z.right
                self.consolidate()
            self.n -= 1
        return z.key if z is not None else None

    def consolidate(self):
        """
        Consolidate trees in the root list to ensure that there is at most one tree of any degree.
        """
        # Estimate the maximum degree.
        D = int(math.log(self.n, 1.618)) + 2 if self.n > 0 else 0
        A = [None] * D

        # Collect all nodes in the root list into an array.
        roots = []
        x = self.min
        if x is not None:
            while True:
                roots.append(x)
                x = x.right
                if x == self.min:
                    break

        for w in roots:
            x = w
            d = x.degree
            while A[d] is not None:
                y = A[d]
                if x.key > y.key:
                    x, y = y, x
                self.heap_link(y, x)
                A[d] = None
                d += 1
            A[d] = x

        self.min = None
        for i in range(D):
            if A[i] is not None:
                if self.min is None:
                    self.min = A[i]
                    A[i].left = A[i]
                    A[i].right = A[i]
                else:
                    # Insert A[i] into the root list.
                    A[i].left = self.min
                    A[i].right = self.min.right
                    self.min.right.left = A[i]
                    self.min.right = A[i]
                    if A[i].key < self.min.key:
                        self.min = A[i]

    def heap_link(self, y, x):
        """
        Link tree y as a child of x.
        """
        # Remove y from the root list.
        y.left.right = y.right
        y.right.left = y.left
        # Make y a child of x.
        y.parent = x
        if x.child is None:
            x.child = y
            y.left = y
            y.right = y
        else:
            y.left = x.child
            y.right = x.child.right
            x.child.right.left = y
            x.child.right = y
        x.degree += 1
        y.mark = False
