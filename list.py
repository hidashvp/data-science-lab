def get_largest_number(numbers):
    if not numbers:
        return None  
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


my_list = [5, 17, 9, 33, 2, 48, 1]
largest_number = get_largest_number(my_list)
print("The largest number is:", largest_number)
