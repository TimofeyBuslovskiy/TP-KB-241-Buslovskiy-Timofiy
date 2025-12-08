from student import Student

class StudentList :
    def __init__(self):
        self.students = []

    def getAll (self) :
        return self.students
    
    def addNewStudent (self, student: Student) :
        insertPosition = 0
        for item in self.students :
            if student.name > item.name :
                insertPosition += 1
            else :
                break
        self.students.insert(insertPosition, student)
    
    def deleteStudent (self, name) :
        for i, student in enumerate(self.students):
            if student.name == name:
                del self.students[i]
                return True
            else :
                print('Student not found')
    
    def findStudent (self, name) :
        for student in self.students :
            if student.name == name :
                return student

    def updateStudent (self, old_name, new_student: Student) :
        target_student = self.findStudent()

        if target_student is not None :
            self.deleteStudent(old_name)
            self.addNewStudent(new_student)
        else :
            print('Student not found')
    

