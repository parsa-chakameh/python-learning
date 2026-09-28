def remove_duplicates(numbers):
    new_list = []
    for number in numbers:
        if number not in new_list:
            new_list.append(number)
    return new_list

numbers = [10, 20, 10, 30, 20, 4, 30, 50]
result = remove_duplicates(numbers)
print(result)