import json
json_str = '{"name":"youngdee", "age": 24}'
student = json.loads(json_str)
print(type(student))
print(student)
