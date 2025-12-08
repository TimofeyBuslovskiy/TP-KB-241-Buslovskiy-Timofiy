import csv
import sys

list = []
 
def load_from_csv (file_name) :
    try :
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader :
                list.append(row)
        print(f"Data loaded seccesful from {file_name}")
    except FileNotFoundError :
        print(f"File {file_name} no found")


def save_csv_data (file_name) :
    try :
        with open(file_name, 'w', encoding='utf-8', newline = '') as file:
            fieldnames = ["name", "phone", "email", "gender"]
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(list)
            print(f'Data saved to {file} seccesfuly')
    except Exception as e:
        print(f'Error to sve data into {file}, error is {e}')


def printAllList():
    for elem in list:
        strForPrint = "Student name is " + elem["name"] + ",  Phone is " + elem["phone"] + ', Email is ' + elem['email'] + ', Gender is ' + elem['gender'] 
        print(strForPrint)
    return

def addNewElement():
    name = input("Pease enter student name: ")
    phone = input("Please enter student phone: ")
    email = input('Please enter your email: ')
    gender = input('Please enter your gender: ')
    newItem = {"name": name, "phone": phone, "email": email, 'gender': gender}
    # find insert position
    insertPosition = 0
    for item in list:
        if name > item["name"]:
            insertPosition += 1
        else:
            break
    list.insert(insertPosition, newItem)
    print("New element has been added")
    return

def deleteElement():
    name = input("Please enter name to be delated: ")
    deletePosition = -1
    for item in list:
        if name == item["name"]:
            deletePosition = list.index(item)
            break
    if deletePosition == -1:
        print("Element was not found")
    else:
        print("Dele position " + str(deletePosition))
        # list.pop(deletePosition)
        del list[deletePosition]
    return


def updateElement():
    
    name = input("Please enter name to be updated: ")
    
    updateStudent = None 
    for student in list :
        if name == student['name'] :
            updateStudent = student
            break
    if not updateStudent :
        print('Student not found')
        return
    print(f"Current details - Name: {updateStudent['name']}, Phone: {updateStudent['phone']}, Email: {updateStudent['email']}, Gender: {updateStudent['gender']}")
    new_name = input(f'Enter new name(leave empty to keep old name "{updateStudent['name']}")') or updateStudent['name']
    new_phone = input(f'Enter new phone(leave empty to keep old phone "{updateStudent['phone']}"') or updateStudent['phone']
    new_email = input(f'Enter new email(leave empty to keep old email "{updateStudent['email']}"') or updateStudent['email'] 
    new_gender = input(f'Enter new gender(leave empty to keep old gender "{updateStudent['gender']}"') or updateStudent['gender']  
    updatedStudent = {'name': new_name, 'phone': new_phone, 'email': new_email, 'gender': new_gender}
    list.remove(updateStudent)
    insertPosition = 0
    for student in list :
        if updatedStudent["name"] > student['name']  :
            insertPosition = insertPosition + 1 
        else:
            break
    list.insert(insertPosition, updatedStudent)
    return    



def main():
    if len(sys.argv) != 2:
        print("Usage: py lab_02.py <csv_file>")
        return
    
    csv_file = sys.argv[1]
    load_from_csv(csv_file)


    while True:
        chouse = input("Please specify the action [ C create, U update, D delete, P print,  X exit ] ")
        match chouse:
            case "C" | "c":
                print("New element will be created:")
                addNewElement()
                printAllList()
            case "U" | "u":
                print("Existing element will be updated")
                updateElement()
            case "D" | "d":
                print("Element will be deleted")
                deleteElement()
            case "P" | "p":
                print("List will be printed")
                printAllList()
            case "X" | "x":
                print("Exit()")
                save_csv_data('students_output.csv')
                break
            case _:
                print("Wrong chouse")


main()