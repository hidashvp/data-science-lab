def find_largest_number(numbers):
    if not numbers:
        return None  # Return None if the list is empty
    largest = numbers[0]
    for number in numbers:
        if number > largest:
            largest = number
    return largest

# Example usage
numbers_list = [5, 12, 3, 89, 45, 67]
largest_number = find_largest_number(numbers_list)
print("The largest number is:", largest_number)
