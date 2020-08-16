a = int(input())
m = a%10
a = a//10
while a > 0:
    if a%10 > m:
        m = a%10
    a = a//10
print(m)

#2 decision

n = int(input('Enter num:'))
my_max = 0
while n > 0:
    residual = n % 10
    if residual > my_max:
        my_max = residual
    n = int(n / 10)
print(my_max)
