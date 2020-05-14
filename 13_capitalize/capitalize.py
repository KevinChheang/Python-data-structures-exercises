def capitalize(phrase):
    """Capitalize first letter of first word of phrase.

        >>> capitalize('python')
        'Python'

        >>> capitalize('only first word')
        'Only first word'
    """
    new_phrase = phrase[0].upper()
    
    # loop through the phrase starting from index 1
    # concat each letter from phrase to new_phrase
    for i in range(1, len(phrase)):
        new_phrase += phrase[i]

    return new_phrase