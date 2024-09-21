# START
num: int = 0
min_number: int = None
max_number: int = None
pos_cnt = 0
neg_cnt = 0
zero: int = 0
seven: int = 0
for i in range(10):
    num: int = int(input('number between 1000-(-1000):'))
    if num == -999:
        break
    if num < -1000 or num > 1000:
        print('not in range...')
        continue

    if max_number == None or num > max_number:
        max_number = num
        pos_cnt += 1

    if min_number == None or num < min_number:
        min_number = num
        neg_cnt += 1

    if num % 7 == 0:
        seven += 1
else:
    print('the loop ended')

    print(f"positive number: {pos_cnt}")
    print(f'negative number: {neg_cnt}')
    print(f'0 entered {zero} times.')
    print(f'number % 7 ==0 entered {seven} times.')
    print(f'the largest number is {max_number}')
    print(f'the smallest number {min_number}')
# END
