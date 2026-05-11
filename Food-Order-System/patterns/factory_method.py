from abc import ABC, abstractmethod
from typing import Protocol
from models.food import Food, Pizza, Burger, Salad


class FoodFactory(ABC):
    """
    Abstract creator class for food factories
    """

    @abstractmethod
    def create_food(self) -> Food:
        """
        Create and return a food item
        """


class PizzaFactory(FoodFactory):
    """Factory for creating Pizza objects"""

    def create_food(self) -> Food:
        return Pizza()


class BurgerFactory(FoodFactory):
    """Factory for creating Burger objects"""

    def create_food(self) -> Food:
        return Burger()


class SaladFactory(FoodFactory):
    """Factory for creating Salad objects"""

    def create_food(self) -> Food:
        return Salad()
