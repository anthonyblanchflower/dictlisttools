def sortbykey(dictlist, sortkey):
    """
    Sort a list of dictionaries by a common key and return the sorted list

        >>> sortbykey([{'A': 3}, {'A': 1}, {'A': 2}])
        [{'A': 1}, {'A': 2}, {'A': 3}]

    :param dictlist: a list of dictionaries sharing a common key
    :param sortkey: a dictionary key used to sort a list of dictionaries
    :return: list of dictionaries sorted by a key
    """
    return sorted(dictlist, key=lambda k: k[sortkey])
