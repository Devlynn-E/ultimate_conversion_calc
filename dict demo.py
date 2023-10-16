my_dict = {
    "blue": "sky",
    "double": 2,
    "half": 0.5,
    "green": "grass",
    "yellow": "sun",
    "red": "apple"
}

your_num = int(input("enter a number: "))
to_do = input("double or half? ").lower()

multiply_by = my_dict[to_do]

answer = your_num * multiply_by
print("{} x {} = {}".format(your_num, multiply_by, answer))
