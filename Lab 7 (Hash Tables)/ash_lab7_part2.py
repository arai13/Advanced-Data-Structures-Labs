"""
Ashutosh Rai
CS 335, Lab 7: Part 2
ash_lab7_part2.py
"""

outer_list_size = 50

hash_table = [[] for x in range(outer_list_size)]  # Hash table using chaining

def hash_function(key):     # Hash function to return the hash value for each key
    return key % outer_list_size


def insert(key, value):     # Function to insert into the hash table
    hash_table[hash_function(key)].append((key, value))


def find_value(key):        # Function to lookup the value based on key
    key_index = hash_function(key)
    list_pairs = hash_table[key_index]
    
    for key_value_pair in list_pairs:
        if key_value_pair[0] == key:
            return key_value_pair[1]
        
    print("The key-value pair you are looking for is not in the hash table")

    
def delete_value(key):      # Function to delete the key-value pair based on key
    key_index = hash_function(key)
    list_pairs = hash_table[key_index]
    
    for key_value_pair in list_pairs:
        if key_value_pair[0] == key:
            list_pairs.remove(key_value_pair)
            return
        
    print("The key-value pair you are looking for is not in the hash table")

print_text = """
************ Student Log ***************

Please enter the number for the correct action:

1 -> Insert a new id and student
2 -> Search for a student
3 -> Delete a student
4 -> Quit
"""
print(print_text)

loop_exit = False
valid_options = ['1','2','3','4']

while loop_exit is False:
    option = input('Enter option >>> ')
    
    while option not in valid_options:
        print("The option you entered is not valid. Please try again.")
        option = input('Enter option>>> ')
    
    if option == '1':
        key = input('Enter the student ID > ')
        value = input('Enter the student name > ')
        insert(int(key), value)
    elif option == '2':
        try:
            key = int(input('Enter the student ID to search > '))
            print(find_value(key))
        except:
            print('The ID is not in the system')
    elif option == '3':
        try:
            key = int(input('Enter the student ID to delete > '))
            delete_value(key)
        except:
            print('The ID is not in the system')
    else:
        loop_exit = True
        
print('Thank you! Have a good day!')