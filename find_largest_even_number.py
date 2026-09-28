def find_largest_even_num(numbers):
    largest_even_num = None
    for number in numbers:
        if largest_even_num is None and number % 2 == 0:
                largest_even_num = number
        elif number > largest_even_num and number % 2 == 0:
            largest_even_num = number
    return largest_even_num

result = find_largest_even_num([-8, -3, -12, -6])
print(result)
    