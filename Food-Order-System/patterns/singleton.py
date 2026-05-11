import threading
from typing import Optional


class RestaurantManager:
    """
    Singleton class responsible for managing restaurant operations

    Ensures only one instance exists using a thread-safe lock
    """
    _instance: Optional["RestaurantManager"] = None
    _lock: threading.Lock = threading.Lock()

    def __init__(self) -> None:
        self.orders = []

    @classmethod
    def get_instance(cls) -> "RestaurantManager":
        """
        Returns the single instance of RestaurantManager (thread-safe)
        """
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = cls()
        return cls._instance

    def add_order(self, order: object) -> None:
        """
        Add a new order to the system
        """
        self.orders.append(order)

