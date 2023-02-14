# 格式化输出
# name = input('What is your name: ')
# age = input('What is your age: ')
# print(f'My name is {name}, my age is {age}')

# 类型转换
# brith_year = int(input('What is your DOB? '))
# age2 = 2023 - brith_year
# print(age2)

# type()方法：查看数据类型
# age = 20
# print(type(age))
# name = 'Rocky'
# print(type(name))

# 索引值：Python 支持通过负数来从右查找对应数据
# name = 'Rocky'
# print(name[0])  # R
# print(name[0:3])  # 打印从索引0到2的字符，不包括最大值 Roc
# print(name[0:])  # 从索引为0的字符打印到结尾 Rocky

# len方法：得到字符串长度
# name = 'Rocky'
# print(len(name))
# name2 = 'Rocky '
# print(len(name2))

# find方法：需要传递一个字符，返回该字符在字符串中的下标,如果字符串中有多个相同字符则返回第一个
# name = 'Rocky so handsome'
# print(name.find('s'))

# if语句练习
# temp = int(input('Enter the temperature: '))
# if temp > 30:
#     print("it's a hot day")
# elif temp < 10:
#     print("it's a cold day")
# else:
#     print('its neither hot or cold')

# name = input('Enter your name please: ')
# if len(name) < 3:
#     print('Name must be at least 3 characters')
# elif len(name) > 10:
#     print('Name can be a maximum of 50 characters')
# else:
#     print('name looks good')

# while loop 练习

is_quit = False
status = ''
while not is_quit:
    user_input = input().lower()
    if user_input == 'start':
        if status == user_input:
            print('Car already started')
        else:
            print('Car started...Ready to go!')
            status = user_input
    elif user_input == 'stop':
        if status == user_input:
            print('Car already stop')
        else:
            print('Car stop')
            status = user_input
    elif user_input == 'quit':
        is_quit = True
    else:
        print('I dont understand that')






