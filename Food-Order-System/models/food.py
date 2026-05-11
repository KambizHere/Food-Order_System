from dataclasses import dataclass


@dataclass
class Food:
    """
    Base class for all food items
    """
    name: str

    def prepare(self) -> str:
        return f"Preparing {self.name}"


class Pizza(Food):
    def __init__(self):
        super().__init__("Pizza")


class Burger(Food):
    def __init__(self):
        super().__init__("Burger")


class Salad(Food):
    def __init__(self):
        super().__init__("Salad")

