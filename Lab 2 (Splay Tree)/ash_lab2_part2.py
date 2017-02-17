"""
Ash Rai
CS 335, Lab 2: Part 2
ash_lab2_part2.py
"""

from ash_lab1_part1 import TreeMap
from ash_lab1_part2 import AVLTreeMap
from ash_lab2_part1 import SplayTreeMap
import time

#Implementations of the trees
hash_map_BST = TreeMap()
hash_map_AVL = AVLTreeMap()
hash_map_Splay = SplayTreeMap()

print("\n--------------------------Insertion Time---------------------------------------")

start_time = time.time()
for i in range(800):
	hash_map_BST[i] = i
print("--- BST Inserting 800 values: %s seconds ---" % (time.time() - start_time))

start_time = time.time()
for i in range(800):
	hash_map_AVL[i] = i
print("--- AVL Tree Inserting 800 values: %s seconds ---" % (time.time() - start_time))

start_time = time.time()
for i in range(800):
	hash_map_Splay[i] = i
print("--- Splay Tree Inserting up 800 values: %s seconds ---\n" % (time.time() - start_time))


print("---------------------------Value look up time----------------------------------")

start_time = time.time()
count = 50
for i in range(500):
	count += i
	hash_map_BST.find_position(count).value()
print("--- BST Tree Looking up 500 values: %s seconds ---" % (time.time() - start_time))

start_time = time.time()
count = 50
for i in range(500):
	count += i
	hash_map_AVL.find_position(count).value()
print("--- AVL Tree Looking up 500 values: %s seconds ---" % (time.time() - start_time))

start_time = time.time()
count = 50
for i in range(500):
	count += i
	hash_map_Splay.find_position(count).value()
print("--- Splay Tree Looking up 500 values: %s seconds ---\n" % (time.time() - start_time))

print("--------------------------Deletion Time---------------------------------------")

start_time = time.time()
for i in range(800):
	hash_map_BST.delete(hash_map_BST.find_position(i))
print("--- BST Deleting 800 values: %s seconds ---" % (time.time() - start_time))

start_time = time.time()
for i in range(800):
	hash_map_AVL.delete(hash_map_AVL.find_position(i))
print("--- AVL Tree Deleting 800 values: %s seconds ---" % (time.time() - start_time))

start_time = time.time()
for i in range(800):
	hash_map_Splay.delete(hash_map_Splay.find_position(i))
print("--- Splay Tree Deleting 800 values: %s seconds ---\n" % (time.time() - start_time))

