from math import floor

def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    last_index = -1
    # convert to lowercase and remove all spaces
    no_space_phrase = phrase.lower().replace(" ", "")
    # get middle index from string
    middle_index = floor(len(no_space_phrase) / 2)

    # loop through string then compare left side with right side
    # if both side the same then word is palindrome
    for i in range(middle_index):
        if no_space_phrase[i] == no_space_phrase[last_index]:
            last_index -= 1
        else:
            return False

    return True




