from dataclasses import dataclass
from typing import List
from models.food import Food


@dataclass
class Order:
    """
    Represents a customer's order consisting of multiple foods
    """
    foods: List[Food]

    def summary(self) -> str:
        """
        Returns a readable summary of all food items in the order
        """
        names = [food.name for food in self.foods]
        return f"Order: {', '.join(names)}"
