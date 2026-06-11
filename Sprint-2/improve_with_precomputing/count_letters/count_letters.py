def count_letters(s: str) -> int:
    """
    count_letters returns the number of letters which only occur in upper case in the passed string.
    """
    char_set = set(s)

    only_upper = {
        char for char in char_set 
        if char.isupper() and char.lower() not in char_set
    }
    return len(only_upper)

