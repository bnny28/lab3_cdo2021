def get_indxs(symbol, string):
    return list(filter(lambda x: x >= 0,
                       map(lambda char, pos: pos if char in symbol else -1,
                           string, range(0, len(string))
                           )
                       ))


first_str = input('Введите первую строку: ')
second_str = input('Введите вторую строку: ')
second_len = len(second_str)

shared_letters = set()
for i in first_str:
    j = 0
    while j < second_len:
        if i not in shared_letters and i == second_str[j]:
            shared_letters.add(i)
            indxs_first_str = get_indxs(i, first_str)
            indxs_sec_str = get_indxs(i, second_str)
            print(f'Общий символ "{i}" в первой строке под индексами {indxs_first_str}, во второй под {indxs_sec_str}')
        j += 1
else:
    print('Общих символов не найдено')
