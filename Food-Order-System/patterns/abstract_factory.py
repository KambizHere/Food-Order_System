from abc import ABC, abstractmethod
from typing import Tuple
from models.food import Food, Pizza, Burger, Salad


class MealPackageFactory(ABC):
    """
    Abstract Factory for creating meal packages
    """

    @abstractmethod
    def create_meal(self) -> Tuple[Food, Food]:
        """
        Returns a tuple of two food items representing a package
        """


class EconomyMealFactory(MealPackageFactory):
    """Creates an economy meal package"""

    def create_meal(self) -> Tuple[Food, Food]:
        return Burger(), Salad()


class NormalMealFactory(MealPackageFactory):
    """Creates a normal meal package."""

    def create_meal(self) -> Tuple[Food, Food]:
        return Pizza(), Salad()


class LuxuryMealFactory(MealPackageFactory):
    """Creates a luxury meal package"""

    def create_meal(self) -> Tuple[Food, Food]:
        return Pizza(), Burger()
