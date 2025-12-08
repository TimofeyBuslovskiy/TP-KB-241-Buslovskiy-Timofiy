import csv
from student import Student

class FileManager :
    @staticmethod
    def load_from_csv(file_name) :
        students = []
        try:
            with open(file_name, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader :
                    student = Student(
                        name = row['name'],
                        phone = row['phone'],
                        email = row['email'],
                        gender = row['gender']
                    )
                    students.append(student)
                print(f'data loaded from {file_name}')
        except FileNotFoundError :
            print(f'File {file_name} not found')
        return students
    

    @staticmethod
    def save_to_csv(file_name, student_list):
        try:
            with open(file_name, 'w', encoding='utf-8', newline='') as file:
                fieldnames = ["name", "phone", "email", "gender"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                writer.writeheader()
                
                for student in student_list:
                    writer.writerow(student.to_dict())
            print(f'data svae to {file_name}')
        except: 
            print(f'error saving to {file_name}')    