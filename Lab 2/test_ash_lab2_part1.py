"""
Ash Rai
CS 335, Lab 1: Part 2
test_ash_lab1_part1.py
"""

import unittest
from ash_lab2_part1 import SplayTreeMap

class SplayTree_TestCase(unittest.TestCase):

	# Building the tree
	def __init__(self, *args, **kwargs):
	   super(SplayTree_TestCase, self).__init__(*args, **kwargs)
	   self.test_tree = SplayTreeMap()
	   self.arr = [5, 9, 2, 6, 20, 15, 23, 18, 12, 13, 32, 21, 14, 16, 7]
	   for i in range(15):
	      self.test_tree[i] = self.arr[i]

	def test_first_value(self):
		self.assertEqual(self.test_tree.first().value(), self.test_tree[0])

	def test_first_key(self):
		self.assertEqual(self.test_tree.first().key(), 0)

	def test_last_value(self):
		self.assertEqual(self.test_tree.last().value(), self.test_tree[14])

	def test_last_key(self):
		self.assertEqual(self.test_tree.last().key(), 14)

	def test_before_key1_is0(self):
		self.assertEqual(self.test_tree.before(self.test_tree.find_position(1)).key(), 0)

	def test_after_key1_is2(self):
		self.assertEqual(self.test_tree.after(self.test_tree.find_position(1)).key(), 2)

	def test_find_min(self):
		self.assertEqual(self.test_tree.find_min()[0], 0)

	def test_find_max(self):
		self.assertEqual(self.test_tree.find_max()[0], 14)

	def test_le(self):
		self.assertEqual(self.test_tree.find_le(5)[0], 5)

	def test_lt(self):
		self.assertEqual(self.test_tree.find_lt(5)[0], 4)

	def test_ge(self):
		self.assertEqual(self.test_tree.find_ge(5)[0], 5)

	def test_gt(self):
		self.assertEqual(self.test_tree.find_gt(5)[0], 6)

	def test_getitem(self):
		self.assertEqual(self.test_tree[0], 5)

	def test_delete(self):
		prev_first = self.test_tree[0]
		self.assertNotEqual(self.test_tree.delete(self.test_tree.find_position(5)), self.test_tree[0])

	def test_setitem(self):
		self.test_tree[0] = 5
		self.assertEqual(self.test_tree[0], 5)

	def test_iter(self):
		list_keys = iter(self.test_tree)
		len_keys = 0
		for i in list_keys:
			len_keys += 1
		self.assertEqual(len_keys, 15)

	def test_reversed(self):
		prev_last = self.test_tree.last().key()
		prev_first = self.test_tree.first().key()
		reversed_tree = list(reversed(self.test_tree))
		new_first = reversed_tree[0]
		new_last = reversed_tree[len(reversed_tree)-1]
		self.assertEqual(new_last, prev_first)
		self.assertEqual(new_first, prev_last)

	def test_delitem(self):
		prev_first = self.test_tree[0]
		del self.test_tree[0]
		self.assertNotEqual(self.test_tree.first().value(), prev_first)

if __name__ == '__main__':
    unittest.main()