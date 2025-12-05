list = [{'name': 'Bob', 'rating': 5},
        {'name': 'Zak', 'rating': 3},
        {'name' : 'Anna', 'rating': 4},
        {'name' : 'Gary', 'rating' : 2}]

while True :
    sortingMethod = input('Change sorting method: n - sorting by name, r - sorting by rating, p - to print list, exit - to end program: ').lower()
    if sortingMethod == 'exit' :
        exit(0)
    elif sortingMethod == 'n':
        for name in sorted(list, key = lambda elem : elem['name']) :
            print(f'Name - {name['name']} | Rating - {name['rating']}')
    elif sortingMethod == 'r':
        for name in sorted(list, key = lambda elem : elem['rating']) :
            print(f'Name - {name['name']} | Rating - {name['rating']}')
    elif sortingMethod == 'p' :
        print(list)