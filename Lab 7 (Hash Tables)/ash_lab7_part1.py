"""
Ashutosh Rai
CS 335, Lab 7: Part 1
ash_lab7_part1.py
"""

# Building of the dictionary, which is implemented using a hash table, for the use case
# Here, the key is the student ID number and the name is the value

student_log = {1434: 'Mark Ruffalo', 2123: 'Rob Stark', 4523: 'Jen Garner', 1246: 'Kina Grannis', 6321: 'Jamie Lannister', 2065: 'Ashutosh Rai', 8876: 'Joe Joe', 9234: 'Anna Kendrick', 5321: 'Liza Thompson', 5623: 'Tommy Lee', 1924: 'Rina Jones', 8988: 'Maggie Wilson'}

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
        student_log[int(key)] = value
    elif option == '2':
        try:
            key = int(input('Enter the student ID to search > '))
            print(student_log[key])
        except:
            print('The ID is not in the system')
    elif option == '3':
        try:
            key = int(input('Enter the student ID to delete > '))
            del student_log[key]
        except:
            print('The ID is not in the system')
    else:
        loop_exit = True
        
print('Thank you! Have a good day!')