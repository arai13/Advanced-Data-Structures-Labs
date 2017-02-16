"""
Ash Rai
CS 335, Lab 2: Part 2
ash_lab4_part2.py
"""

from ash_lab1_part1 import TreeMap
from ash_lab4_part1 import RedBlackTreeMap
import time
import random

#Implementations of the trees
hash_map_BST = TreeMap()
hash_map_RBT = RedBlackTreeMap()

#-------------------------------- Array Generation ------------------------------------
base_array = []

for i in range(800):
	base_array.append(i)

random.shuffle(base_array) #shuffling the array so that they are not sorted

print("\n--------------------------Insertion Time---------------------------------------")

start_time = time.time()
for i in range(800):
	hash_map_BST[i] = base_array[i]
print("--- BST Inserting 800 values: %s seconds ---" % (time.time() - start_time))

start_time = time.time()
for i in range(800):
	hash_map_RBT[i] = base_array[i]
print("--- Red-Black Tree Inserting up 800 values: %s seconds ---\n" % (time.time() - start_time))


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
	hash_map_RBT.find_position(count).value()
print("--- Red-Black Tree Looking up 500 values: %s seconds ---\n" % (time.time() - start_time))


print("--------------------------Deletion Time---------------------------------------")

start_time = time.time()
for i in range(800):
	hash_map_BST.delete(hash_map_BST.find_position(i))
print("--- BST Deleting 800 values: %s seconds ---" % (time.time() - start_time))

start_time = time.time()
for i in range(800):
	hash_map_RBT.delete(hash_map_RBT.find_position(i))
print("--- Red-Black Tree Deleting 800 values: %s seconds ---" % (time.time() - start_time))


