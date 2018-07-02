class Student():
    name = "YoungDee"
    age = "24"
    
    # 每实例化一个对象就使用一次
    def __init__(self, name ,age):
        self.name = name
        self.age = age
        print('student info:')

    def print_student(self):
        print("name:"+self.name)
        print("age:"+str(self.age))
