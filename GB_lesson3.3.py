'''Реализовать функцию my_func(), которая принимает три позиционных
аргумента, и возвращает сумму наибольших двух аргументов.'''
def my_func(num_a , num_s, num_l):
    if num_a >= num_l and num_s >= num_l:
        return num_a + num_s
    elif num_a > num_s and num_a < num_l:
        return num_a + num_l
    else:
         return num_s + num_l

print(f'Result = {my_func(int(input("Enter any num: ")), int(input("Enter second num: ")), int(input("Enter last num: ")))}')