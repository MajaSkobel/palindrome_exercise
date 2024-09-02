def palindrome(word):
    """
    Returns true if a word is a palindrome (word that reads the same forwards as backwards), otherwise false.
    Returns none if the input was not a word.
    """
    if not isinstance(word, str):
        return None
    word_letters = list(word)
    word_letters_reversed = word_letters[::-1]
    return bool(word_letters == word_letters_reversed)
