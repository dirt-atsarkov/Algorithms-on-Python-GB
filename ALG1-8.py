# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
year = int(input('vvedite god: '))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('visokosny god')
else:
    print('nevisokosny god')