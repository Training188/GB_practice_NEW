'''Программа запрашивает у пользователя строку чисел, разделенных
пробелом. При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и
снова нажать Enter. Сумма вновь введенных чисел будет добавляться
к уже подсчитанной сумме. Но если вместо числа вводится специальный
символ, выполнение программы завершается. Если специальный символ
введен после нескольких чисел, то вначале нужно добавить сумму этих
чисел к полученной ранее сумме и после этого завершить программу.'''

def my_sum ():
    sum_result = 0
    ex = True
    while ex == True:
        number = input('Enter 00 for quit - ').split()
        result = 0
        for el in range(len(number)):
            if number[el] == '00':
                ex = False
                break
            else:
                result = result + int(number[el])
        sum_result = sum_result + result
        print(f'Your result: {sum_result}')
        print(f'Your final result: {sum_result}')

my_sum()