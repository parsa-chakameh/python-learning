#second maximum
def second_largest(numbers):
    largest_num = numbers[1]
    second_largest_num = numbers[0]
    for number in numbers:
        if number > largest_num:
            second_largest_num = largest_num
            largest_num = number
        elif number > second_largest_num:
            second_largest_num = number
    return second_largest_num





result = second_largest([10, 5, 20, 8, 15])
print(result)