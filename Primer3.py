a = 23
b = 23

if a > b:
    print("a больше b")
elif a < b:
    print("a меньше b")
else: print("a равно b")

year = 1994
if (year % 400 == 0):
    print("Високосный")
elif (year % 100 == 0):
    print("Не високосный")
elif (year % 4 == 0):
    print("Високосный")
else:
    print("Не високосный")

income = 50000

if (income < 30000):
    print("Низкий доход")
elif (income >= 30000) and (income <= 100000):
    print("Средний доход")
else:
    print("Высокий доход")

start = 1797
rate = 11
threshold = 9461
cycles = 0

while start<=threshold:
    start += start * (rate/100)
    cycles += 1
print(cycles)

n = 12
a = 0
b = 1
cycles = 0

while cycles < n: 
    c = a 
    d = b 
    a = d
    b = c + d
    cycles += 1
print(a)
