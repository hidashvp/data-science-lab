def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as src:
            content = src.read()

        with open(destination_file, 'w') as dest:
            dest.write(content)

        print(f"Contents copied from '{source_file}' to '{destination_file}' successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{source_file}' does not exist.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")


