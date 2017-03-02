"""
Tugii and Ash
CS 335
Lab 5 (Binomial Heap)
File Description: The file contains the implementation of a binomial heap, as well as the tests
"""

import unittest


class PriorityQueue:
    def peek(self):
        raise NotImplementedError

    def pop(self):
        raise NotImplementedError

    def insert(self, key, val):
        raise NotImplementedError


class MergeableHeap:
    def merge(self, other):
        raise NotImplementedError


class BinomialHeap(PriorityQueue, MergeableHeap):
    class ItemRef:
        def __init__(self, node, heap):
            self.item, self.in_tree = node, True
            self.get_heap = heap

    class Node:
        def __init__(self, heap, key, val):
            self.parent, self.next, self.child = None, None, None
            self.red, self.degree = None, 0
            if not val:
                val = key
            self.val, self.key = val, key
            self.item = BinomialHeap.ItemRef(self, heap)

        def add_subtree(self, subtree):
            subtree.parent = self
            subtree.next = self.child
            self.child = subtree
            self.degree += 1

        def decrease_key(self, new_key):
            """Decreases the key of an existing key-value pair."""
            assert new_key <= self.key
            self.key = new_key
            self._bubble()

        def _bubble(self):
            # Bubble Up heap operation
            curr, parent = self, self.parent
            while parent and curr.key < parent.key:
                curr.key, parent.key = parent.key, curr.key
                curr = parent
                parent = curr.parent

        @staticmethod
        def reverse_roots(curr):
            if not curr: return None
            last, next = None, curr
            curr.parent = None
            while curr.next:
                next = curr.next
                curr.next = last
                last = curr
                curr = next
                curr.parent = None
            curr.next = last
            return curr

        @staticmethod
        def merge_roots(heap, other):
            if not heap: return other
            if not other: return heap
            if heap.degree < other.degree:
                new_heap = heap
                heap = new_heap.next
            else:
                new_heap = other
                other = other.next
            parent = new_heap
            while other and heap:
                if heap.degree < other.degree:
                    parent.next = heap
                    heap = heap.next
                else:
                    parent.next = other
                    other = other.next
                parent = parent.next
            if other:
                parent.next = other
            else:
                parent.next = heap
            return new_heap

    class __Item:
        def __init__(self, heap):
            self.heap = heap
            self.item = None

        def get_heap_item(self):
            if self.item:
                self.item = self.item.get_heap_item()
                return self.item

        def get_heap(self):
            return self.get_heap_item().heap

    def __init__(self, lst=[]):
        """The heap can be initialized with a list of key value tuples."""
        self.head = None
        self.size = 0
        self.item = BinomialHeap.__Item(self)
        for item in lst:
            try:
                self.insert(item[0], item[1])
            except TypeError:
                self.insert(item)

    def _min(self):
        """Helper method that returns two nodes with the smallest keys. """
        if not self.head: return None
        min, min_prev = self.head, None
        prev, curr = min, min.next
        while curr:
            if curr.key < min.key:
                min = curr
                min_prev = prev
            prev = curr
            curr = curr.next
        return min, min_prev

    def peek(self):
        """Returns the value with minimum key in the heap."""
        min_pos = self._min()
        return min_pos[0].val if min_pos else None

    def pop(self):
        """Removes the node with the minimum key in the heap."""
        min_pos = self._min()
        if not min_pos: return None
        curr, prev = min_pos
        if prev:
            prev.next = curr.next
        else:
            self.head = curr.next
        children = BinomialHeap.Node.reverse_roots(curr.child)
        self._union(children)
        curr.item.in_tree = False
        self.size -= 1

    def __len__(self):
        """Returns the number of items in the heap."""
        return self.size

    def insert(self, key, val=None):
        node = BinomialHeap.Node(self.item.get_heap, key, val)
        self.size += 1
        self._union(node)
        return node.item

    def _union(self, other):
        if not other or not self.head:
            self.head = other
            return
        heap = BinomialHeap.Node.merge_roots(self.head, other)
        prev, curr, next = None, heap, heap.next
        while next:
            if curr.degree != next.degree or (next.next and next.next.degree == curr.degree):
                prev = curr
                curr = next
            elif curr.key <= next.key:
                curr.next = next.next
                curr.add_subtree(next)
            else:
                if prev:
                    prev.next = next
                else:
                    heap = next
                next.add_subtree(curr)
                curr = next
            next = curr.next
        self.head = heap

    def merge(self, other):
        self.size += other.size
        heap = other.head
        self._union(heap)
        other.item.item = self.item
        other.__init__()


class TestBinomialHeapMethods(unittest.TestCase):
    def setUp(self):
        items = [(30, 'Apple'), (25, 'Paper'), (40, 'Pen')]
        self.heap = BinomialHeap(items)
        self.empty_heap = BinomialHeap()

    def test_peek(self):
        self.assertIsNone(self.empty_heap.peek())
        self.assertEqual(self.heap.peek(), 'Paper')

    def test_pop(self):
        self.assertIsNone(self.empty_heap.pop())
        self.heap.pop()
        self.assertEqual(self.heap.peek(), 'Apple')

    def test_insert(self):
        self.empty_heap.insert(10, 'Orange')
        self.assertEqual(self.empty_heap.peek(), 'Orange')
        self.heap.insert(10, 'Orange')
        self.assertEqual(self.heap.peek(), 'Orange')

    def test_length(self):
        self.assertEqual(len(self.empty_heap), 0)
        self.assertEqual(len(self.heap), 3)
        self.heap.insert(10, 'Orange')
        self.assertEqual(len(self.heap), 4)

    def test_merge_same_degree(self):
        # Same degree
        items2 = [(9, 'Apple'), (26, 'Paper'), (39, 'Pen')]
        other = BinomialHeap(items2)
        temp = self.heap
        temp.merge(other)
        self.assertEqual(len(temp), 6)
        self.assertEqual(temp.peek(), 'Apple')

    def test_merge_diff_degree(self):
        # Different degree
        items2 = [(9, 'Apple'), (39, 'Pen')]
        other = BinomialHeap(items2)
        temp = self.heap
        temp.merge(other)
        self.assertEqual(len(temp), 5)
        self.assertEqual(temp.peek(), 'Apple')

    def test_decrease_key(self):
        self.assertEqual(self.heap.peek(), 'Paper')
        self.heap.head.decrease_key(5)
        self.assertEqual(self.heap.peek(), 'Pen')

if __name__ == '__main__':
    unittest.main()
