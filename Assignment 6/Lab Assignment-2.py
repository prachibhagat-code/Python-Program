# Lab Assignment 2
# Copy python script without comments

source_file = input("Enter the source python file name: ")
destination_file = input("Enter the destination file name: ")

try:
    with open(source_file, "r") as f1, open(destination_file, "w") as f2:
        for line in f1:
            stripped = line.strip()

            # Ignore comment lines
            if not stripped.startswith("#"):
                # Remove inline comments
                if "#" in line:
                    line = line.split("#")[0] + "\n"

                f2.write(line)

    print("\nFile copied without comments successfully.")

    print("\nContent of Source File:\n")
    with open(source_file, "r") as f1:
        print(f1.read())

    print("\nContent of Destination File:\n")
    with open(destination_file, "r") as f2:
        print(f2.read())

except FileNotFoundError:
    print("Source file not found.")