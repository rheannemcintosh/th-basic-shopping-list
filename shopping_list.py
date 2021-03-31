shopping_list = []

def add_to_list(item):
    shopping_list.append(item)
    print("Added {} to the List! List now has {} item.".format(item, len(shopping_list)))

def show_help():
    print("What should we buy today? ")
    print("""
        Enter 'DONE' to stop adding items.
        Enter 'HELP' for this help.
        """)

show_help()

while True:
    new_item = input('> ')

    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()