def find_second_largest(numbers):
    max_num = numbers[0]
    second_max = None
        
    for number in numbers:
        if second_max is None:
            if number > max_num:
                second_max = max_num
                max_num = number
            elif number != max_num:
                second_max = number
        else:
            if number > max_num:
                second_max = max_num
                max_num = number
            elif number > second_max and number != max_num:
                second_max = number
    return second_max

numbers = [20, 20, 20, 45, 2,3,5,76,7,76,5,46,56,75,6,74,56,45,4,32,42,33,12,31,21,1]
result = find_second_largest(numbers)
print(result)

