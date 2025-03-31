def add(add_item):
    if add_item not in initial_menu and add_item!=None:
        initial_menu.append(add_item)
def remove(remove_item):
    if remove_item in initial_menu:
        initial_menu.remove(remove_item)
    else:
        print(f'{remove_item} is not there in initial_menu')
def check(check_item):
    if check_item in initial_menu:
        print(f'Availability:"{check_item} is Available" ')
def updated():
    print(f'Updated menu:{initial_menu}')

initial_menu=["Pizza", "Burger", "Pasta", "Salad"]
remove('Salad')
add('Tacos')
updated()
check(input('Search the Food: '))

