#По введенным пользователем координатам двух точек вывести уравнение прямой вида
#y = kx + b, проходящей через эти точки.

x1 = int(input("Enter x1"))
x2 = int(input("Enter x2"))
y1 = int(input("Enter y1"))
y2 = int(input("Enter y2"))

b = y1 - x1 * (y2 - b) / x1
