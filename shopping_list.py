# ---------------------------------------------------------------- #
#
# shopping_list.py
#
# This is a sample project created to create a simple Python
# shopping list via the command line. Built in conjuntion with the
# Python Introducing Lists course at teamtreehouse.com
#
# Author:  Rheanne McIntosh <rheanne.mcintosh@outlook.com>
# Created: November 2020
#
# ---------------------------------------------------------------- #


# Function to add an item to a list
def add_to_list(item):
    shopping_list.append(item)
    print(
        "Added {} to the List! List now has {} item."
        .format(item, len(shopping_list)))


# Function to display command line help to the user
def show_help():
    print("What should we buy today? ")
    print("""
        Enter 'DONE' to stop adding items.
        Enter 'HELP' for this help.
        Enter 'SHOW' to display the shopping list.
        """)


# Function to display the shopping list to the user
def show_list():
    print("Here is your list:")
    for item in shopping_list:
        print(item)


# Declare an empty shopping list
shopping_list = []

# Display the help when the user first opens the program
show_help()

# Use a loop for user input
while True:
    new_item = input('> ')

    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue

    add_to_list(new_item)

# Display the final shopping list
show_list()
