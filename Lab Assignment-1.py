# Lab Assignment 1
# Read a file and write its contents in uppercase to another file

source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")

try:
    # Open source file
    with open(source_file, "r") as f1:
        content = f1.read()

    # Convert to uppercase
    upper_content = content.upper()

    # Write to destination file
    with open(destination_file, "w") as f2:
        f2.write(upper_content)

    print("\nContent successfully written in uppercase.")

    # Display output file content
    print("\nContent of destination file:")
    with open(destination_file, "r") as f2:
        print(f2.read())

except FileNotFoundError:
    print("Source file not found.")