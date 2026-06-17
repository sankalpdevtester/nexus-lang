import time
from typing import Any, Dict

class Cache:
    def __init__(self, ttl: int = 60):
        """
        Initialize the cache with a time-to-live (TTL) in seconds.

        Args:
        ttl (int): The time-to-live in seconds. Defaults to 60.
        """
        self.cache: Dict[str, Any] = {}
        self.ttl = ttl

    def get(self, key: str) -> Any:
        """
        Get a value from the cache.

        Args:
        key (str): The key to retrieve.

        Returns:
        Any: The cached value or None if not found or expired.
        """
        if key in self.cache:
            value, expiry = self.cache[key]
            if time.time() < expiry:
                return value
            else:
                del self.cache[key]
        return None

    def set(self, key: str, value: Any) -> None:
        """
        Set a value in the cache.

        Args:
        key (str): The key to store.
        value (Any): The value to store.
        """
        expiry = time.time() + self.ttl
        self.cache[key] = (value, expiry)

    def delete(self, key: str) -> None:
        """
        Delete a key from the cache.

        Args:
        key (str): The key to delete.
        """
        if key in self.cache:
            del self.cache[key]

    def clear(self) -> None:
        """
        Clear the entire cache.
        """
        self.cache.clear()


def create_cache(ttl: int = 60) -> Cache:
    """
    Create a new cache instance.

    Args:
    ttl (int): The time-to-live in seconds. Defaults to 60.

    Returns:
    Cache: A new cache instance.
    """
    return Cache(ttl)


# Example usage:
if __name__ == "__main__":
    cache = create_cache(ttl=30)
    cache.set("example_key", "example_value")
    print(cache.get("example_key"))  # Output: example_value
    time.sleep(31)
    print(cache.get("example_key"))  # Output: None