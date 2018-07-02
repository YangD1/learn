# 简单的函数使用:
def add(x,y):
    result  = x+y
    return result

print(add(1,2))

print("函数返回多个结果:")
# 函数返回多个结果
def damage(skill1, skill2):
    damage1 = skill1 * 3
    damage2 = skill1 * 2 + 10 
    #  返回一个元组
    return damage1, damage2
    
damages = damage(3,6)
print(type(damages))
# 改变函数回调参数的接收方式,这种方式叫作：序列解包
skill1_mamage, skill2_damage = damage(3,6)
print(skill1_mamage, skill2_damage)

print("可变参数：")
# 可变参数
def demo(*param):
    print(param)
    print(type(param))

demo(1,2,3,4,5,6)

# 面向对象
print("python 面向对象")
class Student():
    name = 'YoungDee'
    age = '24' 

    # self 来调用类自己的属性和方法
    def print_file(self):
        print('name:'+self.name)
        print('age:'+self.age)
       
# 实例化对象
student  = Student() 
student.print_file()
