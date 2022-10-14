# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

num = list(input('Input number: '))
num.sort()
x = num.count(',')
y = num.count('.')
num.reverse()
if x > 0 or y > 0:
    num.pop()

sum=0
h=0
i=0

while i < len(num):
    h=int(num[i])

    sum+=h
    i=i+1

print('Sum of digits= ', sum)
