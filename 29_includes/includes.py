def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    # check if collectioin is of type "str", "list" or "tuple"
    if type(collection) == str or type(collection) == list or type(collection) == tuple:
        # if start index is provided
        # search collection from start index
        if start:
            for i in range(start, len(collection)):
                if sought == collection[i]:
                    return True
        # else if start index is not provided
        # search whole collection
        elif sought in collection:
            return True
    # check for type of "set"
    # ignore start index even if given, because unorder data structure
    elif type(collection) == set:
        for item in collection:
            if sought == item:
                return True
    # check for type of "dict"
    # ignore start index even if given, because unorder data structure
    elif type(collection) == dict:
        for (k, v) in collection.items():
            if sought == v:
                return True

    return False
