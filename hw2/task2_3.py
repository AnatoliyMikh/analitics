# Задайте список (словарь не нужно выводить!) из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

a = list()
n = int(input('Input N: '))

sum = 0
i = 1

while i<=n:
    a.append((1 + 1 / i)**i)
    i+=1
    sum = sum + a[-1] 

print('sum of numbers = ',sum)