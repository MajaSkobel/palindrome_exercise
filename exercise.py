def palindrome(word):
    """
    Returns true if a word is a palindrome (word that reads the same forwards as backwards), otherwise false.
    Returns none if the input was not a word.
    """
    if not isinstance(word, str):
        return None
    return bool(list(word) == list(word)[::-1])
