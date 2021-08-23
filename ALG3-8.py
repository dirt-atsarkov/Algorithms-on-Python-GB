# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

mylist = [[0 for n in range(4)] for n in range(4)]

for i in range(4):
    for j in range(4):
        mylist[i][j] = int(input())
    mylist[i].append(sum(mylist[i]))

for i in mylist:
    print(i, end="\n")