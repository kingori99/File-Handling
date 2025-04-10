def process_file(input_filename, output_filename):
    """
    Reads the content of an input file, modifies it, and writes
    the modified content to a new output file.

    Args:
        input_filename (str): The name of the file to read from.
        output_filename (str): The name of the file to write to.
    """
    try:
        with open(input_filename, 'r') as infile:
            content = infile.readlines()  # Read all lines into a list

        modified_content = [line.strip().upper() + " (PROCESSED)\n" for line in content]

        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)

        print(f"Successfully processed '{input_filename}' and wrote to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError:
        print(f"Error: Could not read or write to the file(s).")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def get_valid_filename():
    """
    Prompts the user for a filename and handles potential errors
    if the file doesn't exist or cannot be read.

    Returns:
        str: A valid filename that exists and can be read, or None if an error occurs.
    """
    while True:
        filename = input("Enter the filename to read: ")
        try:
            with open(filename, 'r') as f:
                # Attempt to read a line to check if the file is readable
                f.readline()
            return filename
        except FileNotFoundError:
            print(f"Error: The file '{filename}' was not found. Please try again.")
        except IOError:
            print(f"Error: Could not read the file '{filename}'. Please check permissions and try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")
        print() # Add an empty line for better readability

if __name__ == "__main__":
    # File Read & Write Challenge
    input_file = "input_challenge.txt"
    output_file = "output_challenge.txt"

    # Create a sample input file if it doesn't exist
    try:
        with open(input_file, 'x') as f:
            f.write("This is line one.\n")
            f.write("Another line of text.\n")
            f.write("Processing files is fun!\n")
    except FileExistsError:
        pass # File already exists, no need to create

    process_file(input_file, output_file)
    print("\n" * 2) # Add extra spacing

    # Error Handling Lab
    valid_input_filename = get_valid_filename()

    if valid_input_filename:
        print(f"\nYou entered a valid filename: '{valid_input_filename}'.")
        # You could now proceed to do something with this valid filename
        # For example, you could call process_file again if you wanted
        # to write a different modified version.
    else:
        print("\nNo valid filename was provided.")
