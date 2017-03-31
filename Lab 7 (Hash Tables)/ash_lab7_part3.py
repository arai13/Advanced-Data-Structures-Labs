"""
Ashutosh Rai
CS 335, Lab 7: Part 3
ash_lab7_part3.py
"""

import random
import string
import time

#----------------------------- My Hash Table Implementation -------------------------------
outer_list_size = 100000

hash_table = [[] for x in range(outer_list_size)]  # Hash table using chaining

def hash_function(key): 	# Hash function to return the hash value for each key
    return key % outer_list_size


def insert(key, value):  	# Function to insert into the hash table
    hash_table[hash_function(key)].append((key, value))


def find_value(key): 		# Function to lookup the value based on key
    key_index = hash_function(key)
    list_pairs = hash_table[key_index]
    
    for key_value_pair in list_pairs:
        if key_value_pair[0] == key:
            return key_value_pair[1]
        
    print("The key-value pair you are looking for is not in the hash table")

    
def delete_value(key):		# Function to delete the key-value pair based on key
    key_index = hash_function(key)
    list_pairs = hash_table[key_index]
    
    for key_value_pair in list_pairs:
        if key_value_pair[0] == key:
            list_pairs.remove(key_value_pair)
            return
        
    print("The key-value pair you are looking for is not in the hash table")

#------------------------------------------------------------------------------


list_ID = random.sample(range(1000000), 100000) # Generation of random ID numbers
list_names = []
student_log = {}

for i in range(100000):
    name = random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase) + " " + random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase)
    list_names.append(name)


    


print('------ Test Results for 100000 pairs (Python Dictionary vs. My Hash Table) -------\n')
    
#---------------- Test to insert all the key-value pair ---------------------

# For the dictionary
start_time = time.time()

for i in range(100000):
    student_log[list_ID[i]] = list_names[i]
    
print("Insertion time for the Python dictionary: %s seconds" % (time.time() - start_time))

# For my hash table
start_time = time.time()

for i in range(100000):
    insert(list_ID[i], list_names[i])
    
print("Insertion time for the my hash table: %s seconds\n" % (time.time() - start_time))



#---------------- Test to search all the key-value pair ---------------------

# For the dictionary
start_time = time.time()

for i in range(100000):
    student_log[list_ID[i]]
    
print("Searching time for the Python dictionary: %s seconds" % (time.time() - start_time))

# For my hash table
start_time = time.time()

for i in range(100000):
    find_value(list_ID[i])
    
print("Searching time for the my hash table: %s seconds\n" % (time.time() - start_time))


#---------------- Test to delete all the key-value pair ---------------------

# For the dictionary
start_time = time.time()

for i in range(100000):
    del student_log[list_ID[i]]
    
print("Deletion time for the Python dictionary: %s seconds" % (time.time() - start_time))

# For my hash table
start_time = time.time()

for i in range(100000):
    delete_value(list_ID[i])
    
print("Deletion time for the my hash table: %s seconds" % (time.time() - start_time))
