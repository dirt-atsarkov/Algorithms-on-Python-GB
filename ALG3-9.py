# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random
import numpy

mylist = [[random.randint(0, 100) for n in range(3)] for n in range(3)]
print(*mylist, sep='\n')

mylist = numpy.array(mylist)
mylist = mylist.transpose()
newlist = mylist.tolist()
mylist = [0, 0, 0]

for i in range(3):
    mylist[i] = min(newlist[i])

print(f"MAX of 3 MINS {mylist} is {max(mylist)}")
# print(min_num)