import json
# 反序列化
# json_str = '{"name":"youngdee", "age": 24}'
# student = json.loads(json_str)
# print(type(student))
# print(student)


# 序列化
student = [
    {'name': 'YoungDee', 'age': 24, 'flag': False},
    {'name': 'Mona', 'age': 18}
]
json_str = json.dumps(student)
print(type(json_str))
print(json_str)
