def count_vowels (word : str) -> int:
    """
    This functions returns the number of vowels in a word
    """
    vowels: int = 0
    for char in word:
        if char.lower() in ('a','e','i','o','u'):
            vowels += 1
    return vowels