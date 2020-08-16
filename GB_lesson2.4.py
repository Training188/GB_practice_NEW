'''Пользователь вводит строку из нескольких слов, разделённых
пробелами. Вывести каждое слово с новой строки.
Строки необходимо пронумеровать. Если в слово длинное,
выводить только первые 10 букв в слове.'''

my_list = input("Enter a string separated by commas: ")
my_word = []
num = 1
for el in range(my_list.count(' ') + 1):
    my_word = my_list.split()
    if len(str(my_word)) <= 10:
        print(f"{num}: {my_word [el]}")
        num += 1
    else:
        print(f"{num} {my_word [el] [0:10]}")
        num += 1