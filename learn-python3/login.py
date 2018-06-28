'''
简单的使用逻辑运算符
'''
account = 'youngdee'
password = 'a111222a'

print("输入您的账号：")
user_account = input()
print("输入您的密码：")
user_password = input()

if account == user_account and password == user_password:
    print('success')
else:
    print('fail')
