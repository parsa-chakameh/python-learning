#second maximum
def second_largest(numbers):
    largest_num = None
    second_largest_num = None
    for number in numbers:
        if largest_num is None or number > largest_num:
            second_largest_num = largest_num
            largest_num = number
        elif second_largest_num is None and number != largest_num or (number != largest_num and second_largest_num < number):
            second_largest_num = number
    return second_largest_num

result = second_largest([20, 10, 5])
print(result)