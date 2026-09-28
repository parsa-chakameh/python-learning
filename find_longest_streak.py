def find_longest_streak(numbers):
    num1 = 1
    num2 = 0
    longest = 1
    if len(numbers) != 0:
        for number in numbers:
            if number == num2:
                num1 = num1 + 1
                if num1 > longest:
                    longest = num1
            else:
                num2 = number
                num1 = 1
    else:
        longest = 0
    return longest
numbers = [2, 3, 3, 3, 3, 3, 4, 4, 5, 5,5,5 ,5 ,5,55,55,555,5,5,5,5,5,5,5,5,5,5,5,6,6,6,6,6,66,6,6,66,7,7,7,7,8,7,7,]
result = find_longest_streak(numbers)
print(result)