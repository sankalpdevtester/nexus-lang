import time

def now():
    """
    Get the current time in seconds since the epoch.
    
    Returns:
        float: The current time.
    """
    return time.time()

def sleep(seconds):
    """
    Pause execution for the specified number of seconds.
    
    Args:
        seconds (float): The number of seconds to sleep.
    """
    time.sleep(seconds)

def type_of(x):
    """
    Get the type of the input value.
    
    Args:
        x: The input value.
    
    Returns:
        str: The type of the input value.
    """
    return type(x).__name__

def is_number(x):
    """
    Check if the input value is a number.
    
    Args:
        x: The input value.
    
    Returns:
        bool: True if the input value is a number, False otherwise.
    """
    return isinstance(x, (int, float))

def is_string(x):
    """
    Check if the input value is a string.
    
    Args:
        x: The input value.
    
    Returns:
        bool: True if the input value is a string, False otherwise.
    """
    return isinstance(x, str)

def is_list(x):
    """
    Check if the input value is a list.
    
    Args:
        x: The input value.
    
    Returns:
        bool: True if the input value is a list, False otherwise.
    """
    return isinstance(x, list)