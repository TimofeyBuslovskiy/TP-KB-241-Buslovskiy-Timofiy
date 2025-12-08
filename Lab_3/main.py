import sys
from student import Student
from student_list import StudentList
from utils import FileManager

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <csv_file>")
        return

    csv_file = sys.argv[1]
    group_list = StudentList()
    loaded_data = FileManager.load_from_csv(csv_file)
    for student in loaded_data:
        group_list.addNewStudent(student)

    while True:
        choice = input("Please specify the action [ C create, U update, D delete, P print, X exit ]: ")
        match choice.lower():
            case "c":
                print("New element will be created:")
                name = input("Please enter student name: ")
                phone = input("Please enter student phone: ")
                email = input("Please enter your email: ")
                gender = input("Please enter your gender: ")
                
                new_student = Student(name, phone, email, gender)
                group_list.addNewStudent(new_student)
                print("New element has been added")

            case "u":
                print("Existing element will be updated")
                name = input("Please enter name to be updated: ")
                student = group_list.findStudent(name)
                
                if student:
                    print(f"Current details - {student}")
                    new_name = input(f'Enter new name (leave empty to keep "{student.name}"): ') or student.name
                    new_phone = input(f'Enter new phone (leave empty to keep "{student.phone}"): ') or student.phone
                    new_email = input(f'Enter new email (leave empty to keep "{student.email}"): ') or student.email
                    new_gender = input(f'Enter new gender (leave empty to keep "{student.gender}"): ') or student.gender
                    
                    updated_student_obj = Student(new_name, new_phone, new_email, new_gender)
                    group_list.updateStudent(name, updated_student_obj)
                    print("Element updated")
                else:
                    print("Student not found")

            case "d":
                print("Element will be deleted")
                name = input("Please enter name to be deleted: ")
                if group_list.deleteStudent(name):
                    print("Element deleted")
                else:
                    print("Element was not found")

            case "p":
                print("List will be printed")
                for student in group_list.getAll():
                    print(student)

            case "x":
                print("Exit()")
                FileManager.save_to_csv('students_output.csv', group_list.getAll())
                break
            case _:
                print("Wrong choice")

if __name__ == "__main__":
    main()