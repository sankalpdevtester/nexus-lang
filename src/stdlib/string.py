def length(s):
    """
    Compute the length of the input string.
    
    Args:
        s (str): The input string.
    
    Returns:
        int: The length of the input string.
    """
    return len(s)

def concat(s1, s2):
    """
    Concatenate two strings.
    
    Args:
        s1 (str): The first string.
        s2 (str): The second string.
    
    Returns:
        str: The concatenated string.
    """
    return s1 + s2

def substring(s, start, end):
    """
    Extract a substring from the input string.
    
    Args:
        s (str): The input string.
        start (int): The start index.
        end (int): The end index.
    
    Returns:
        str: The extracted substring.
    """
    return s[start:end]

def index(s, substr):
    """
    Find the index of the first occurrence of the specified substring in the input string.
    
    Args:
        s (str): The input string.
        substr (str): The substring to find.
    
    Returns:
        int: The index of the substring if found, -1 otherwise.
    """
    try:
        return s.index(substr)
    except ValueError:
        return -1

def to_upper(s):
    """
    Convert the input string to uppercase.
    
    Args:
        s (str): The input string.
    
    Returns:
        str: The uppercase string.
    """
    return s.upper()

def to_lower(s):
    """
    Convert the input string to lowercase.
    
    Args:
        s (str): The input string.
    
    Returns:
        str: The lowercase string.
    """
    return s.lower()

def split(s, sep):
    """
    Split the input string into substrings separated by the specified separator.
    
    Args:
        s (str): The input string.
        sep (str): The separator.
    
    Returns:
        list: The list of substrings.
    """
    return s.split(sep)