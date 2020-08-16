co_profit = int(input('Enter profit company:'))
co_lesion = int(input('Enter lesion company:'))
if co_profit > co_lesion:
    print('Good Job my friend')
    print(f'Your profin result: {co_profit / co_lesion}')
else:
    print('You need change tactice')
co_unit = int(input('Enter numbers of unit:'))
print(f'profit from 1 unit: {co_profit/co_unit}')
