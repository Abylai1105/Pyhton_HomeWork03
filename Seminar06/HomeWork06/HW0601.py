# 1- Определить, присутствует ли в заданном списке строк, некоторое число

# Ма6ма сш3ы9л24а мн0е ш4та7ны из 34бер8ёзо34в1ой ко235ры
inp_text = 'Ма6ма сш3ы9л24а мн0е ш4та7ны из 34бер8ёзо34в1ой ко235ры'.split()
print(inp_text)

find_num = int(input('Введите число: '))


def get_word(text, find_number):
    return list(filter(lambda element: str(find_number) in element, text))


find_word = get_word(inp_text, find_num)
print(find_word)