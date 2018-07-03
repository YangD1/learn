class Student():
    name = "Mona"
    def __init__(self):
        print(self.__class__.name)

    def createStudent(self):
        print("success created")

    @staticmethod
    def add():
        print("static create success")
    

s1 = Student()
s1.createStudent()
s1.add()