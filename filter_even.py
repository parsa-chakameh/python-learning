def filter_even(numbers):
    list = []
    for number in numbers:
        if number % 2 == 0:
            list.append(number)
    return list

new_list = filter_even([3, 8, 15, 22, 7, 10, 19, 4])
print(new_list)
