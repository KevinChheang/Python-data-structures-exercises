def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    # easy way to just use the predefined method
    # return phrase.title()

    # my own implementation of title()
    split_phrase = phrase.lower().split(" ")
    titleize_word = ""

    for word in split_phrase:
        if word != split_phrase[-1]:
            titleize_word += word.capitalize() + " "
        else:
            titleize_word += word.capitalize()

    return titleize_word
