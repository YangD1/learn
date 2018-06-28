print('hello, world')
print(type(1*1))
print('hello \\n world')
print(type([1,2,3,4,5,6]))
print([1,2,3]+[4,5,6])
print(type((1,2,3,4,5)))
print("hello world"[2:8:2])
print(1 in [1,2,3,4,5,6])
print(10 in [1,2,3,4,5,6])
print(max([1,2,3,4,5,6,7,8.1]))
print(min([1,2,3,4,5,6,7,8.1]))
print(max("YoungDee"))
# 空字典
print(type({}))
print({'Q':"PHP",'W':"JavaScript","E":"Go","R":"Python"})
print({'Q':"PHP",'W':"JavaScript","E":"Go","R":"Python"}['Q'])
print({'Q':"PHP",'W':"JavaScript","E":"Go","R":"Python"}['R'])

# 变量
A = [1,2,3,4,5,6]
print(A)

a = [1,2,3,4,5,6]
a[0] = "a";
print(a);

a = 1
b = a 
a = 3
print(a)
print(b)

a = [1,2,3]
b = a
a[0] = "a"
print(a)
print(b)

a = 'hello'
a = a + " world"
print(a)

print(hex(id(a)))
# 取出元组中列表的数字4
a = (1,2,3,[1,2,4])
print(a[3][2])

b = 2
a = 3
b += a
print(b)
b -= a
print(b)
b *= a
print(b)

print(True and True)
print(True and False)
print(True or False)
print(False or False)
print(not False)
print(not True)
print(not '')
print(not '0')
print([] or [])

a = {1,2,3}
b = {2,1,3}
print(a == b) # 集合是无序的，所有显示的True
print(a is b) # 两个变量的内存地址不一样，所以显示的False

c = (1,2,3)
d = (2,1,3)
print(c == d) # 元组是序列，有序的，所以是False 
print(c is d) # 内存地址不同，所以是False

a = "youngdee"
print(isinstance(a,(int,float,str)))

a = 1
b = 2
c = 3
print(a + b * c)
print(a or b and c)

# python 使用缩进来标示代码块
mood = True
if mood:
    print('go to left')
else :
    print('go to right')


# 判断变量是否为空
d = []
if d :
    print('不为空')
else:
    print('为空')

# 判断变量符合后嵌套判断输出正确的返回值
#a = input()    
a = 1
a = int(a)
if a == 1:
    print('apple')
elif a == 2:
    print('orange')
elif a == 3:
    print('banana')
else:
    print('noshopping')


a = 1
b = 0
c = a or b
print(c)
    
print("--------------------------------------------------------")
print("while 递归循环:")
counter = 0
while counter <= 10 :
    counter += 1
    print(counter)
else:
    print('EOF')

print("--------------------------------------------------------")
print("for 遍历循环")
a = [['apple','orange','banan','grape'],(1,2,3)]
for x in a:
    for y in x:
        print(y)
else:
    print('fruit is gone')

print("--------------------------------------------------------")
print("for 条件循环，循环0到10")
# range() 函数， 第一个参数:起始数值，第二个参数：偏移量，第三个参数：步长(可以使负数实现降序排列)
for x in range(0,10):
    print(x)

#for x in range(0,10,2):
#    print(x,end=' | ')

a = [1,2,3,4,5,6,7,8]
for i in range(0, len(a), 2):
    print(a[i], end=" | ")


b = a[0:len(a):2]
print(b)


# 高性能，封装性（可复用）,抽象
# 直白

