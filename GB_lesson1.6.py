import math
f_day_result = int(input(''))
need_res = int(input(''))
result = f_day_result
n_day = 1
print(f'Day {n_day} your result {result}')
while need_res > result:
        result += result * 0.1
        n_day += 1
        print(f'Day {n_day} your result {result}')


