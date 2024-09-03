def add(numbers: str) -> int:
    if numbers == "":
        return 0
    else:
        num_lst = numbers.split(",")
        return sum(int(num) for num in num_lst)
