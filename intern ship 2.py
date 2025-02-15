def count_words(text):
    """
    Function to count the number of words in a given text.
    :param text: str, input text from user
    :return: int, word count
    """
    words = text.split()
    return len(words)


def main():
    """
    Main function to handle user input and display the word count.
    """
    print("Welcome to the Word Counter Program!")
    user_input = input("Enter a sentence or paragraph: ").strip()
    
    if not user_input:
        print("Error: No input provided. Please enter some text.")
        return
    
    word_count = count_words(user_input)
    print(f"Word Count: {word_count}")


if __name__ == "__main__":
    main()
