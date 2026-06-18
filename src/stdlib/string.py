def length(s):
    """
    Returns the length of a string.

    Args:
        s (str): The string.

    Returns:
        int: The length of the string.
    """
    return len(s)

def concat(a, b):
    """
    Concatenates two strings together.

    Args:
        a (str): The first string.
        b (str): The second string.

    Returns:
        str: The concatenated string.
    """
    return a + b

def substring(s, start, end):
    """
    Returns a substring of a string.

    Args:
        s (str): The string.
        start (int): The start index.
        end (int): The end index.

    Returns:
        str: The substring.
    """
    return s[start:end]

def index_of(s, substr):
    """
    Returns the index of the first occurrence of a substring in a string.

    Args:
        s (str): The string.
        substr (str): The substring to find.

    Returns:
        int: The index of the substring.

    Raises:
        ValueError: If the substring is not found in the string.
    """
    try:
        return s.index(substr)
    except ValueError:
        raise ValueError("Substring not found in string")

def to_uppercase(s):
    """
    Converts a string to uppercase.

    Args:
        s (str): The string.

    Returns:
        str: The uppercase string.
    """
    return s.upper()

def to_lowercase(s):
    """
    Converts a string to lowercase.

    Args:
        s (str): The string.

    Returns:
        str: The lowercase string.
    """
    return s.lower()