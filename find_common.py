def find_unique_common(numbers1, numbers2):
    new_list = []
    for number in numbers1:
        if number not in numbers2 and number not in new_list:
            new_list.append(number)
    return new_list

numbers1 = [1, 4, 7, 9, 12]
numbers2 = [2, 4, 6, 7, 10, 12]
result = find_unique_common(numbers1, numbers2)
print(result)