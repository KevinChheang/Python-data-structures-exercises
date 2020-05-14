def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """
    freq_count = 0;

    for char in lst:
        if char == search_term:
            freq_count += 1
    
    return freq_count