# Take input from the user
search_word = input("Enter the word to search: ")
replace_word = input("Enter the word to replace it with: ")

# Open and read the original file
file = open("old.txt", "r")
content = file.read()
file.close()

# Replace the word
content = content.replace(search_word, replace_word)

# Write the modified content to a new file
file = open("new.txt", "w")
file.write(content)
file.close()

print("Word replaced successfully in 'new.txt'")