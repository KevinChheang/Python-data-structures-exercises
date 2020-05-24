def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which are not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = "aeiou"
    lst = list(s)
    i = 0
    counter = len(s) - 1

    while i < counter:
        if lst[i].lower() not in vowels:
            i += 1
        elif lst[counter].lower() not in vowels:
            counter -= 1
        else:
            temp = lst[i]
            lst[i] = lst[counter]
            lst[counter] = temp
            i += 1
            counter -= 1

    return "".join(lst)
