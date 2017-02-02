"""
Ash Rai
CS 335, Lab 1: Part 3
ash_lab1_part3.py
File Description: BST and AVL Tree used as a Hash map. The map represents the number and the name of the players of my favorite soccer team Chelsea FC.
"""

from ash_lab1_part1 import TreeMap
from ash_lab1_part2 import AVLTreeMap

# Array holding the players name in order of the number
arr = ['Courtois', 'Alonso', 'Azplizueta', 'Cahill', 'Luiz', 'Moses', 'Kante', 'Matic', 'Hazard', 'Pedro', 'Willian', 'Costa']

#------------------------------------------- BST Implementation ----------------------------------------------------

hash_map_BST = TreeMap()
for i in range(12):
   hash_map_BST[i] = arr[i]


#------------------------------------------- AVL Implementation ----------------------------------------------------

hash_map_AVL = AVLTreeMap()
for i in range(12):
   hash_map_AVL[i] = arr[i]
