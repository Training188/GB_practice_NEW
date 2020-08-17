'''Реализовать функцию, принимающую два числа
(позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя,
предусмотреть обработку ситуации деления на ноль.'''


def div(*args):

    try:
        arg1 = int(input("Enter f_arg  "))
        arg2 = int(input("Enter s_arg "))
        res = arg1 / arg2
    except ValueError:
        return 'Not integer type'
    except ZeroDivisionError:
        return "You can't divide by zero!"

    return res

    if arg2 != 0:
        return arg1 / arg2
    else:
        print("You can't divide by zero.")


print(f'result  {div()}')