from random import randint
from typing import List
def get_unique_list_numbers() -> List[int]:
    list_num = []
    while len(list_num) < 15:
        random_num = randint(-10, 10)
        if random_num not in list_num:
            list_num.append(random_num)
    return list_num


list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
