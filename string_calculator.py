import re


def add(numbers: str) -> int:
    if numbers == "":
        return 0
    else:
        if numbers.startswith("//"):
            delimiter, numbers = numbers[2:].split("\n", 1)
            num_lst = numbers.split(delimiter)
        else:
            num_lst = re.split(",|\n|;", numbers)
        return sum(int(num) for num in num_lst)
