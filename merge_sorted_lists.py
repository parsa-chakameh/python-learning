def merge_sorted_lists(numbers1, numbers2):
    new_list = []
    index1 = 0
    index2 = 0
    while index1 < len(numbers1) and index2 < len(numbers2):
        if numbers1[index1] < numbers2[index2]:
            new_list.append(numbers1[index1])
            index1 += 1
        elif numbers1[index1] > numbers2[index2]:
            new_list.append(numbers2[index2])
            index2 += 1
        else:
            new_list.append(numbers2[index2])
            index2 += 1
    while index1 < len(numbers1):
        new_list.append(numbers1[index1])
        index1 += 1
    while index2 < len(numbers2):
        new_list.append(numbers2[index2])
        index2 += 1
    return new_list
numbers1 = [1, 4, 7, 10]
numbers2 = [2, 3, 6, 8, 12]
result = merge_sorted_lists(numbers1, numbers2)
print(result)