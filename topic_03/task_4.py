def findPosition(sorted_list, new_el) :
    for i, element in enumerate(sorted_list):
        if new_el <= element:
            return i
    return len(sorted_list)

def addElInSortedList(sorted_list, new_el) :
    position = findPosition(sorted_list, new_el)
    
    sorted_list.insert(position, new_el)
    return sorted_list

sorted_list = [1, 2, 3, 5, 6, 7, 8, ]
new_element = 4

print('Sorted list', sorted_list)
updated_list_  = addElInSortedList(sorted_list, new_element)
print('Updated list: ', updated_list_)  



