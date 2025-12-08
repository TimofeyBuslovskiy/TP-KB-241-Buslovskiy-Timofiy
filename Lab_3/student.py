class Student :
    def __init__(self, name, phone, email, gender):
        self.name = name
        self.phone = phone
        self.email = email
        self.gender = gender
    
    def __str__(self):
        return f"Student name is {self.name}, student phone is {self.phone}, student email is {self.email}, student gender is {self.gender}"
    
    def to_dict (self) :
        return {
            "name": self.name,
            "phone": self.phone,
            "email": self.email,
            "gender": self.gender
        }