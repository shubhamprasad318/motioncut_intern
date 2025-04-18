# -*- coding: utf-8 -*-

def count_words(text):
    """
    Counts the number of words in the given text.

    Parameters:
        text (str): The input string to count words from.

    Returns:
        int: The total number of words.
    """
    # Split the text using whitespace as the delimiter and return the length of the resulting list.
    words = text.split()
    return len(words)

def main():
    """
    Main function to handle user input and display the word count.
    """
    # Prompt the user for input
    user_input = input("Please enter a sentence or paragraph: ").strip()

    # Error handling: Check if the input is empty
    if not user_input:
        print("Error: No input provided. Please enter some text next time.")
        return

    # Count the words in the user input using the count_words function
    word_count = count_words(user_input)

    # Display the output
    print(f"The total number of words is: {word_count}")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
