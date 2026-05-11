import unittest
from patterns.abstract_factory import (
    EconomyMealFactory,
    NormalMealFactory,
    LuxuryMealFactory,
)
from models.food import Pizza, Burger, Salad, Food


class TestAbstractFactoryPattern(unittest.TestCase):
    # 1
    def test_economy_meal_returns_two_items(self) -> None:
        """Economy meal should return exactly two food items."""
        main, side = EconomyMealFactory().create_meal()
        self.assertIsInstance(main, Food)
        self.assertIsInstance(side, Food)

    # 2
    def test_normal_meal_returns_two_items(self) -> None:
        """Normal meal should return exactly two food items."""
        main, side = NormalMealFactory().create_meal()
        self.assertIsInstance(main, Food)
        self.assertIsInstance(side, Food)

    # 3
    def test_luxury_meal_returns_two_items(self) -> None:
        """Luxury meal should return exactly two food items."""
        main, side = LuxuryMealFactory().create_meal()
        self.assertIsInstance(main, Food)
        self.assertIsInstance(side, Food)

    # 4
    def test_economy_meal_contains_burger_and_salad(self) -> None:
        """Economy meal should contain Burger as main and Salad as side."""
        main, side = EconomyMealFactory().create_meal()
        self.assertIsInstance(main, Burger)
        self.assertIsInstance(side, Salad)

    # 5
    def test_normal_meal_contains_pizza_and_salad(self) -> None:
        """Normal meal should contain Pizza as main and Salad as side."""
        main, side = NormalMealFactory().create_meal()
        self.assertIsInstance(main, Pizza)
        self.assertIsInstance(side, Salad)

    # 6
    def test_luxury_meal_contains_pizza_and_burger(self) -> None:
        """Luxury meal should contain Pizza as main and Burger as side."""
        main, side = LuxuryMealFactory().create_meal()
        self.assertIsInstance(main, Pizza)
        self.assertIsInstance(side, Burger)

    # 7
    def test_all_factories_return_food_instances(self) -> None:
        """All factories must only return Food instances."""
        for factory in (
            EconomyMealFactory(),
            NormalMealFactory(),
            LuxuryMealFactory(),
        ):
            main, side = factory.create_meal()
            self.assertIsInstance(main, Food)
            self.assertIsInstance(side, Food)

    # 8
    def test_meals_from_same_factory_have_new_instances(self) -> None:
        """Two calls to the same factory should produce new instances."""
        factory = NormalMealFactory()
        main1, side1 = factory.create_meal()
        main2, side2 = factory.create_meal()

        self.assertIsNot(main1, main2)
        self.assertIsNot(side1, side2)

    # 9
    def test_meal_items_have_non_empty_names(self) -> None:
        """Returned food items should have non-empty names."""
        factories = [EconomyMealFactory(), NormalMealFactory(), LuxuryMealFactory()]
        for factory in factories:
            main, side = factory.create_meal()
            self.assertIsInstance(main.name, str)
            self.assertIsInstance(side.name, str)
            self.assertGreater(len(main.name), 0)
            self.assertGreater(len(side.name), 0)

    # 10
    def test_combinations_between_factories_are_different(self) -> None:
        """Each factory should represent a different meal combination."""
        eco_main, eco_side = EconomyMealFactory().create_meal()
        norm_main, norm_side = NormalMealFactory().create_meal()
        lux_main, lux_side = LuxuryMealFactory().create_meal()

        self.assertNotEqual(
            (type(eco_main), type(eco_side)),
            (type(norm_main), type(norm_side)),
        )
        self.assertNotEqual(
            (type(norm_main), type(norm_side)),
            (type(lux_main), type(lux_side)),
        )


if __name__ == "__main__":
    print("Running tests...")
    unittest.main()
    print("All tests finished.")

