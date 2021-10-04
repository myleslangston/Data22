def vowel_consonant_reader(string):
    """Counts the number of vowels and consonants in a string"""
    # Creates a list of the words in the string
    letters = string.lower().split(" ")
    # Turns the list into a list of characters
    list_letters = ''.join(letters)
    vowels = ["a", "e", "i", "o", "u"]
    vowel_count = 0
    consonant_count = 0
    # Iterates through each character in the string
    for char in list_letters:
        # Checks to see if each character in the list is a letter or not
        if char.isalpha():
            # If it's a letter, follows the loop below and adds to the counters
            if char in vowels:
                vowel_count += 1
            elif char not in vowels:
                consonant_count += 1
    print(f"The vowel count is {vowel_count}.\nThe consonant count is {consonant_count}.")


vowel_consonant_reader(input("Please write a sentence: "))

