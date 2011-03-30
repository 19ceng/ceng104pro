import doctest

def recursive_min(nested_num_list):
    """
      >>> recursive_min([2, 9, [1, 13], 8, 6])
      1
      >>> recursive_min([2, [[100, 1], 90], [10, 13], 8, 6])
      1
      >>> recursive_min([2, [[13, -7], 90], [1, 100], 8, 6])
      -7
      >>> recursive_min([[[-13, 7], 90], 2, [1, 100], 8, 6])
      -13
    """

def recursive_count(target, nested_num_list):
    """
      >>> recursive_count(2, [2, 9, [2, 1, 13, 2], 8, [2, 6]])
      4
      >>> recursive_count(7, [[9, [7, 1, 13, 2], 8], [7, 6]])
      2
      >>> recursive_count(15, [[9, [7, 1, 13, 2], 8], [2, 6]])
      0
      >>> recursive_count(5, [[5, [5, [1, 5], 5], 5], [5, 6]])
      6
    """


def flatten(nested_num_list):
    """
      >>> flatten([2, 9, [2, 1, 13, 2], 8, [2, 6]])
      [2, 9, 2, 1, 13, 2, 8, 2, 6]
      >>> flatten([[9, [7, 1, 13, 2], 8], [7, 6]])
      [9, 7, 1, 13, 2, 8, 7, 6]
      >>> flatten([[9, [7, 1, 13, 2], 8], [2, 6]])
      [9, 7, 1, 13, 2, 8, 2, 6]
      >>> flatten([[5, [5, [1, 5], 5], 5], [5, 6]])
      [5, 5, 1, 5, 5, 5, 5, 6]
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod()

