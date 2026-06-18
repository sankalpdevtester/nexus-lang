def length(lst):
    """
    Returns the length of a list.

    Args:
        lst (list): The list.

    Returns:
        int: The length of the list.
    """
    return len(lst)

def append(lst, item):
    """
    Appends an item to the end of a list.

    Args:
        lst (list): The list.
        item: The item to append.

    Returns:
        list: The modified list.
    """
    lst.append(item)
    return lst

def insert(lst, index, item):
    """
    Inserts an item at a specific index in a list.

    Args:
        lst (list): The list.
        index (int): The index to insert at.
        item: The item to insert.

    Returns:
        list: The modified list.
    """
    lst.insert(index, item)
    return lst

def remove(lst, item):
    """
    Removes the first occurrence of an item in a list.

    Args:
        lst (list): The list.
        item: The item to remove.

    Returns:
        list: The modified list.

    Raises:
        ValueError: If the item is not found in the list.
    """
    if item not in lst:
        raise ValueError("Item not found in list")
    lst.remove(item)
    return lst

def index_of(lst, item):
    """
    Returns the index of the first occurrence of an item in a list.

    Args:
        lst (list): The list.
        item: The item to find.

    Returns:
        int: The index of the item.

    Raises:
        ValueError: If the item is not found in the list.
    """
    try:
        return lst.index(item)
    except ValueError:
        raise ValueError("Item not found in list")

def slice(lst, start, end):
    """
    Returns a slice of a list.

    Args:
        lst (list): The list.
        start (int): The start index.
        end (int): The end index.

    Returns:
        list: The slice of the list.
    """
    return lst[start:end]