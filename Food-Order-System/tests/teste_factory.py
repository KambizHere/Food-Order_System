import unittest
from patterns.factory_method import PizzaFactory, BurgerFactory, SaladFactory
from models.food import Pizza, Burger, Salad, Food


class TestFactoryMethodPattern(unittest.TestCase):
    # 1
    def test_pizza_factory_creates_pizza_instance(self) -> None:
        """PizzaFactory should create a Pizza instance."""
        factory = PizzaFactory()
        product = factory.create_food()
        self.assertIsInstance(product, Pizza)

    # 2
    def test_burger_factory_creates_burger_instance(self) -> None:
        """BurgerFactory should create a Burger instance."""
        factory = BurgerFactory()
        product = factory.create_food()
        self.assertIsInstance(product, Burger)

    # 3
    def test_salad_factory_creates_salad_instance(self) -> None:
        """SaladFactory should create a Salad instance."""
        factory = SaladFactory()
        product = factory.create_food()
        self.assertIsInstance(product, Salad)

    # 4
    def test_all_factories_return_food_subclass(self) -> None:
        """All factories must return subclasses of Food."""
        factories = [PizzaFactory(), BurgerFactory(), SaladFactory()]
        for factory in factories:
            self.assertIsInstance(factory.create_food(), Food)

    # 5
    def test_pizza_factory_sets_correct_name(self) -> None:
        """PizzaFactory product should have name 'Pizza'."""
        product = PizzaFactory().create_food()
        self.assertEqual(product.name, "Pizza")

    # 6
    def test_burger_factory_sets_correct_name(self) -> None:
        """BurgerFactory product should have name 'Burger'."""
        product = BurgerFactory().create_food()
        self.assertEqual(product.name, "Burger")

    # 7
    def test_salad_factory_sets_correct_name(self) -> None:
        """SaladFactory product should have name 'Salad'."""
        product = SaladFactory().create_food()
        self.assertEqual(product.name, "Salad")

    # 8
    def test_pizza_prepare_returns_expected_message(self) -> None:
        """Pizza.prepare should return a non-empty preparation message."""
        product = PizzaFactory().create_food()
        message = product.prepare()
        self.assertIsInstance(message, str)
        self.assertGreater(len(message), 0)
        self.assertIn("Pizza", message)

    # 9
    def test_burger_prepare_returns_expected_message(self) -> None:
        """Burger.prepare should mention Burger in the message."""
        product = BurgerFactory().create_food()
        message = product.prepare()
        self.assertIn("Burger", message)

    # 10
    def test_salad_prepare_returns_expected_message(self) -> None:
        """Salad.prepare should mention Salad in the message."""
        product = SaladFactory().create_food()
        message = product.prepare()
        self.assertIn("Salad", message)


if __name__ == "__main__":
    print("Running tests...")
    unittest.main()
    print("All tests finished.")
