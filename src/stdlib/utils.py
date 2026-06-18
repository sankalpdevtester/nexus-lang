import time

def now():
    """
    Returns the current time in seconds since the epoch.

    Returns:
        float: The current time.
    """
    return time.time()

def sleep(seconds):
    """
    Pauses execution for a specified amount of time.

    Args:
        seconds (float): The amount of time to sleep.
    """
    time.sleep(seconds)

def type_of(obj):
    """
    Returns the type of an object.

    Args:
        obj: The object.

    Returns:
        str: The type of the object.
    """
    return type(obj).__name__

def is_instance_of(obj, type_):
    """
    Checks if an object is an instance of a specific type.

    Args:
        obj: The object.
        type_: The type to check.

    Returns:
        bool: True if the object is an instance of the type, False otherwise.
    """
    return isinstance(obj, type_)