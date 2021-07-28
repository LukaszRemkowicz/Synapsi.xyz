from typing import Any, List
from itertools import product


"""TASK #1"""


def reverse_int(number: Any) -> int:

    try:
        reversed_num = int(''.join(str(number)[::-1]))
        result = reversed_num
    except:
        reversed_num = ''.join(str(number)[-1:0:-1])
        result = 0 - int(reversed_num)

    return 0 if 0 < int(reversed_num) >= abs(number) else int(result)


# print(reverse_int(-5927694924))


"""TASK #2"""


def check_product(digits: Any) -> List:
    letters = {
        '1': '',
        '2': list('ABC'),
        '3': list('DEF'),
        '4': list('GHI'),
        '5': list('JKL'),
        '6': list('MNO'),
        '7': list('PQRS'),
        '8': list('TUV'),
        '9': list('WXYZ'),
        '0': list('+'),
    }

    help_list = [letters[num] for num in str(digits)]

    products = product(*help_list)

    return [''.join(element) for element in products]


# print(check_product(46))


""" TASK #3 """


def maximum_string(string: str, max_width: int) -> str:
    counter = 0

    result = []
    new_string = []

    for element in string.split(' '):

        if len(element) > max_width:
            break

        if counter <= max_width and (counter + len(element)) <= max_width:
            counter += len(element) + 1
            new_string.append(element)
        else:
            counter = 0
            new_string.append('\n')
            result.append(' '.join(new_string))
            new_string.clear()
            new_string.append(element)
            counter += len(element) + 1

        if counter >= max_width or element == string.split(' ')[-1]:
            counter = 0
            new_string.append('\n')
            result.append(' '.join(new_string))
            new_string.clear()

    result.insert(0, '[\n')
    result.insert(len(result), ']')

    return (' '.join(result)).replace('\n ', '\n')


max_string = maximum_string("Hey there mate, it’s nice to finally meet you!", 16)

# print(max_string)








