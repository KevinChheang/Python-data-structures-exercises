def mode(nums):
    """Return most-common number in list.

    For this function, there will always be a single-most-common value;
    you do not need to worry about handling cases where more than one item
    occurs the same number of times.

        >>> mode([1, 2, 1])
        1

        >>> mode([2, 2, 3, 3, 2])
        2
    """
    # dictionary to hold frequency values
    freq_dict = {}

    # add num to dictioinary and count frequency
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1

    # get most frequence value (most occurence)
    max_number = max(freq_dict.values())

    # find the most frequence index
    for (key, value) in freq_dict.items():
        if value == max_number:
            return key

