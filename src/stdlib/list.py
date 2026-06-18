def length(lst):
    """
    Compute the length of the input list.
    
    Args:
        lst (list): The input list.
    
    Returns:
        int: The length of the input list.
    """
    return len(lst)

def append(lst, item):
    """
    Append an item to the input list.
    
    Args:
        lst (list): The input list.
        item: The item to append.
    
    Returns:
        list: The modified list.
    """
    lst.append(item)
    return lst

def insert(lst, index, item):
    """
    Insert an item at the specified index in the input list.
    
    Args:
        lst (list): The input list.
        index (int): The index to insert at.
        item: The item to insert.
    
    Returns:
        list: The modified list.
    """
    lst.insert(index, item)
    return lst

def remove(lst, item):
    """
    Remove the first occurrence of the specified item in the input list.
    
    Args:
        lst (list): The input list.
        item: The item to remove.
    
    Returns:
        list: The modified list.
    """
    lst.remove(item)
    return lst

def sort(lst):
    """
    Sort the input list in ascending order.
    
    Args:
        lst (list): The input list.
    
    Returns:
        list: The sorted list.
    """
    return sorted(lst)

def reverse(lst):
    """
    Reverse the input list.
    
    Args:
        lst (list): The input list.
    
    Returns:
        list: The reversed list.
    """
    return lst[::-1]

def index(lst, item):
    """
    Find the index of the first occurrence of the specified item in the input list.
    
    Args:
        lst (list): The input list.
        item: The item to find.
    
    Returns:
        int: The index of the item if found, -1 otherwise.
    """
    try:
        return lst.index(item)
    except ValueError:
        return -1