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
# is_quit = False
# stop = True
# while not is_quit:
#     user_input = input().lower()
#     if user_input == 'start':
#         if stop:
#             stop = False
#             print('Car started...Ready to go!')
#         else:
#             print('Car already started')
#     elif user_input == 'stop':
#         if stop:
#             print('Car already stop')
#         else:
#             stop = True
#             print('Car stop')
#     elif user_input == 'quit':
#         is_quit = True
#     else:
#         print('I dont understand that')

# for loop 练习
# 1.遍历字符串
# for item in "Rocky so handsome":
#     print(item)
# # 2.遍历数组
# for item in ['Rocky', 'Lucia']:
#     print(item)
# # 3.通过range方法遍历设定的数字范围
# for item in range(1,11):
#     print(item)
# # 使用for loop 计算数组中数字的和
# prices = [10, 20, 30]
# total_price = 0
# for item in prices:
#     total_price += item
# print(total_price)

# for循环嵌套练习
# numbers = [5, 2, 5, 2, 2]
# for item in numbers:
#     output = ''
#     for item2 in range(item):
#         output += 'x'
#     print(output)

# 找到数组中的最大数字
# number_list = [3, 3, 4, 9, 9, 6, 8, 10, 100, 2, 1, 5, 13]
# large_number = number_list[0]
# for item in number_list:
#     if item >= large_number:
#         large_number = item
# print(large_number)
