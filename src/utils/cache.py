import time
from typing import Any, Dict

class Cache:
    def __init__(self, ttl: int = 60):
        """
        Initialize the cache with a time-to-live (TTL) in seconds.

        Args:
        ttl (int): The time-to-live for cache entries in seconds. Defaults to 60.
        """
        self.ttl = ttl
        self.cache: Dict[str, Any] = {}
        self.expiration_times: Dict[str, float] = {}

    def get(self, key: str) -> Any:
        """
        Get a value from the cache.

        Args:
        key (str): The key to retrieve from the cache.

        Returns:
        Any: The cached value if it exists and has not expired, otherwise None.
        """
        if key in self.cache:
            if time.time() < self.expiration_times[key]:
                return self.cache[key]
            else:
                del self.cache[key]
                del self.expiration_times[key]
        return None

    def set(self, key: str, value: Any) -> None:
        """
        Set a value in the cache.

        Args:
        key (str): The key to store in the cache.
        value (Any): The value to store in the cache.
        """
        self.cache[key] = value
        self.expiration_times[key] = time.time() + self.ttl

    def delete(self, key: str) -> None:
        """
        Delete a key from the cache.

        Args:
        key (str): The key to delete from the cache.
        """
        if key in self.cache:
            del self.cache[key]
            del self.expiration_times[key]

    def clear(self) -> None:
        """
        Clear all entries from the cache.
        """
        self.cache.clear()
        self.expiration_times.clear()

def get_cache() -> Cache:
    """
    Get a singleton instance of the cache.

    Returns:
    Cache: The singleton cache instance.
    """
    if not hasattr(get_cache, 'instance'):
        get_cache.instance = Cache()
    return get_cache.instance

# Example usage:
cache = get_cache()
cache.set('example_key', 'example_value')
print(cache.get('example_key'))  # Output: example_value
time.sleep(61)  # Wait for the TTL to expire
print(cache.get('example_key'))  # Output: None