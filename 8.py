def capitalize_words_in_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            lines = src.readlines()

        with open(destination_file, 'w') as dest:
            for line in lines:
                words = line.split()
                capitalized_words = [word.upper() for word in words]
                dest.write(' '.join(capitalized_words) + '\n')

        print(f"Capitalized content written to '{destination_file}'.")

    except FileNotFoundError:
        print(f"Error: File '{source_file}' not found.")
    except IOError as e:
        print(f"I/O error occurred: {e}")
