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

    nve_num = [num for num in num_lst if int(num) < 0]
    if nve_num:
        raise ValueError(f"negative numbers not allowed {(', ').join(nve_num)}")

    num_lst = [int(num) for num in num_lst if int(num) < 1000]

    return sum(num_lst)
