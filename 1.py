def remove_duplicates(original_list):
    seen = set()
    unique_list = []
    for item in original_list:
        if item not in seen:
            unique_list.append(item)
            seen.add(item)
    return unique_list

my_list = [1, 3, 5, 3, 7, 1, 9, 5]
no_duplicates = remove_duplicates(my_list)
print("List after removing duplicates:", no_duplicates)
