import re
# language = 'PythonC#JavaC#PHPC#'
# # 这里的 0 代表匹配所有的都替换，替换别的数字将会按顺序按数量替换
# r = re.sub('C#','GO',language,0)
# print(r)

# # >> PythonGOJavaGOPHPGO

# # re.sub() 第二个参数还可以是函数
# def convert(value):
#     print(value)

# r = re.sub('C#',convert,language)
# print(r)


# 实现字符串中大于等于6的数字统一替换成9
# s = 'A8C3721D86'
# def convert(value):
#     matched = value.group()
#     if int(matched) >= 6:
#         return str(9)
#     else: 
#         return str(0)

# r = re.sub('\d',convert,s)
# print(r)
import re
s = 'life is short,i use python'
r = re.search('life(.*)python',s)
print(r.group(1))
# >>  is short,i use

print(r.group(0))
# >> life is short,i use python

# 下面将返回一个元组结果
print(r.group(0,1))
