import unittest
from patterns.builder import OrderBuilder
from models.food import Pizza, Burger, Salad
from models.order import Order


class TestOrderBuilderPattern(unittest.TestCase):
    # 1
    def test_builder_creates_order_instance(self) -> None:
        """Builder should create an Order instance."""
        builder = OrderBuilder()
        order = builder.build()
        self.assertIsInstance(order, Order)

    # 2
    def test_add_single_food_to_order(self) -> None:
        """Adding one food item should appear in the order."""
        pizza = Pizza()
        builder = OrderBuilder()
        order = builder.add_food(pizza).build()

        self.assertEqual(len(order.foods), 1)
        self.assertIs(order.foods[0], pizza)

    # 3
    def test_add_multiple_foods_preserves_order(self) -> None:
        """Adding multiple foods should preserve insertion order."""
        pizza = Pizza()
        burger = Burger()
        salad = Salad()

        order = (
            OrderBuilder()
            .add_food(pizza)
            .add_food(burger)
            .add_food(salad)
            .build()
        )

        self.assertEqual(
            [food.name for food in order.foods],
            ["Pizza", "Burger", "Salad"],
        )

    # 4
    def test_order_summary_returns_correct_string(self) -> None:
        """Order summary should return a correct formatted string."""
        pizza = Pizza()
        burger = Burger()
        order = OrderBuilder().add_food(pizza).add_food(burger).build()
        self.assertEqual(order.summary(), "Order: Pizza, Burger")

    # 5
    def test_builder_accumulates_items_across_multiple_build_calls(self) -> None:
        """Builder should keep previously added items unless explicitly reset."""
        builder = OrderBuilder()
        pizza = Pizza()
        burger = Burger()

        builder.add_food(pizza)
        first_order = builder.build()

        builder.add_food(burger)
        second_order = builder.build()

        self.assertEqual(len(second_order.foods), 2)
        self.assertIs(second_order.foods[0], pizza)
        self.assertIs(second_order.foods[1], burger)

    # 6
    def test_empty_order_has_empty_foods_list(self) -> None:
        """Order created without foods should have an empty list."""
        order = OrderBuilder().build()
        self.assertEqual(order.foods, [])

    # 7
    def test_add_food_returns_builder_for_chaining(self) -> None:
        """add_food should return the builder instance to allow chaining."""
        builder = OrderBuilder()
        pizza = Pizza()
        returned = builder.add_food(pizza)

        self.assertIs(returned, builder)

    # 8
    def test_order_contains_exact_number_of_items_added(self) -> None:
        """Number of foods in order should match number of add_food calls."""
        builder = OrderBuilder()
        builder.add_food(Pizza()).add_food(Burger())
        order = builder.build()

        self.assertEqual(len(order.foods), 2)

    # 9
    def test_order_foods_are_same_objects_passed_in(self) -> None:
        """Foods stored in order should be the exact passed-in instances."""
        pizza = Pizza()
        burger = Burger()
        order = OrderBuilder().add_food(pizza).add_food(burger).build()

        self.assertIs(order.foods[0], pizza)
        self.assertIs(order.foods[1], burger)

    # 10
    def test_summary_for_single_item_order(self) -> None:
        """Summary for a single item order should contain only that item."""
        pizza = Pizza()
        order = OrderBuilder().add_food(pizza).build()
        self.assertEqual(order.summary(), "Order: Pizza")


if __name__ == "__main__":
    print("Running tests...")
    unittest.main()
    print("All tests finished.")
