class Student :
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Student: name= {self.name}, age= {self.age}"
    
    def __repr__(self):
        return self.__str__()

students = [
    Student('Bob', 20),
    Student('Zak', 18),
    Student('Anna', 23),
    Student('Kate', 22)
]

while True :
    sortingMethod = input('Change sorting method: n - sorting by name, a - sorting by age, p - to print list, exit - to end program: ').lower()
    if sortingMethod == 'exit' :
        exit(0)
    elif sortingMethod == 'n':
        students = sorted(students, key = lambda student: student.name)
    elif sortingMethod == 'a':
        students = sorted(students, key = lambda student: student.age)
    elif sortingMethod == 'p' :
        print(students)