def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """
    reverse_str = ""
    index = -1
    for char in phrase:
        if abs(index) <= len(phrase):
            reverse_str += phrase[index]
            index -= 1

    return reverse_str        
