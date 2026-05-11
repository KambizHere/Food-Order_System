from models.order import Order
from models.food import Food
from typing import List, Optional


class OrderBuilder:
    """
    Builder pattern for constructing Order objects step by step
    """

    def __init__(self) -> None:
        self._foods: List[Food] = []

    def add_food(self, food: Food) -> "OrderBuilder":
        """
        Add a food item to the order.
        """
        self._foods.append(food)
        return self

    def build(self) -> Order:
        """
        Finalize and return the constructed order object
        """
        return Order(foods=self._foods)
