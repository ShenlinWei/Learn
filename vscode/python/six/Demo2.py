account = 'qiyue'
password = '123456'

print('please input account')
user_account=input()
print('please input password')
user_password = input()

if(account==user_account and user_password==password) :
    print('success')
else:
    print('fail')