# custom_module.py

def reverse_string(s):
    """
    Reverses the given string.
    """
    return s[::-1]

def capitalize_string(s):
    """
    Capitalizes the first letter of the given string.
    """
    return s.capitalize()

def main():
    """
    Main function to demonstrate string manipulation.
    """
    input_string = input("Enter a string: ").strip()  # Remove extra spaces from input

    # Reverse and capitalize the string
    reversed_string = reverse_string(input_string)
    capitalized_string = capitalize_string(input_string)

    # Display results
    print(f"Reversed string: {reversed_string}")
    print(f"Capitalized string: {capitalized_string}")

if __name__ == "__main__":
    main()