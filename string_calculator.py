import re


def add(numbers: str) -> int:
    if numbers == "":
        return 0
    else:
        num_lst = re.split(",|\n", numbers)
        return sum(int(num) for num in num_lst)
