"""
Ash Rai
CS 335, Lab 1: Part 1
ash_lab1_part1_test.py
"""

import unittest
from ash_lab1_part1 import TreeMap

class BST_TestCase(unittest.TestCase):

	# Buildint the tree
	def __init__(self, *args, **kwargs):
	   super(BST_TestCase, self).__init__(*args, **kwargs)
	   self.test_tree = TreeMap()
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

	def test_test_le(self):
		self.assertEqual(self.test_tree.find_le(5)[0], 5)

	def test_test_lt(self):
		self.assertEqual(self.test_tree.find_lt(5)[0], 4)

	def test_test_ge(self):
		self.assertEqual(self.test_tree.find_ge(5)[0], 5)

	def test_test_gt(self):
		self.assertEqual(self.test_tree.find_gt(5)[0], 6)

if __name__ == '__main__':
    unittest.main()