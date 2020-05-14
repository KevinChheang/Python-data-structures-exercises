def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_phrase = ""
    letter = ""

    for char in phrase:
        # convert "to_swap" to lowercase then compare
        # if it's the same, change "char" to uppercase
        # vice versa with "elif" statement
        if char == to_swap.lower():
            letter = char.upper()
        elif char == to_swap.upper():
            letter = char.lower()
        else:
            letter = char

        new_phrase += letter
    return new_phrase