import unittest
from patterns.singleton import RestaurantManager
from models.order import Order
from models.food import Pizza, Burger


class TestRestaurantManagerSingleton(unittest.TestCase):
    def setUp(self) -> None:
        # Ensure we start with a clean state for each test
        manager = RestaurantManager.get_instance()
        manager.orders.clear()

    # 1
    def test_get_instance_returns_same_object(self) -> None:
        """get_instance should always return the same singleton object."""
        a = RestaurantManager.get_instance()
        b = RestaurantManager.get_instance()
        self.assertIs(a, b)

    # 2
    def test_orders_list_shared_between_instances(self) -> None:
        """Orders list must be shared across all singleton references."""
        manager1 = RestaurantManager.get_instance()
        manager2 = RestaurantManager.get_instance()

        order = Order(foods=[Pizza()])
        manager1.add_order(order)

        self.assertEqual(len(manager2.orders), 1)
        self.assertIs(manager2.orders[0], order)

    # 3
    def test_add_order_appends_to_orders(self) -> None:
        """add_order should append a new order to the orders list."""
        manager = RestaurantManager.get_instance()
        order = Order(foods=[Pizza()])
        manager.add_order(order)
        self.assertIn(order, manager.orders)

    # 4
    def test_multiple_orders_are_kept_in_insertion_order(self) -> None:
        """Multiple orders should be stored in insertion order."""
        manager = RestaurantManager.get_instance()
        order1 = Order(foods=[Pizza()])
        order2 = Order(foods=[Burger()])
        manager.add_order(order1)
        manager.add_order(order2)

        self.assertEqual(manager.orders[0], order1)
        self.assertEqual(manager.orders[1], order2)

    # 5
    def test_orders_list_initially_empty_after_clear(self) -> None:
        """After manual clear, orders list should be empty."""
        manager = RestaurantManager.get_instance()
        self.assertEqual(len(manager.orders), 0)

    # 6
    def test_singleton_instance_not_recreated_by_multiple_calls(self) -> None:
        """Calling get_instance multiple times must not create a new instance."""
        first = RestaurantManager.get_instance()
        for _ in range(5):
            self.assertIs(first, RestaurantManager.get_instance())

    # 7
    def test_orders_reference_same_list_object(self) -> None:
        """orders attribute should reference the same list object across instances."""
        manager1 = RestaurantManager.get_instance()
        manager2 = RestaurantManager.get_instance()
        self.assertIs(manager1.orders, manager2.orders)

    # 8
    def test_add_order_increases_length_by_one(self) -> None:
        """Adding one order should increase the orders length by exactly one."""
        manager = RestaurantManager.get_instance()
        before = len(manager.orders)
        manager.add_order(Order(foods=[Pizza()]))
        after = len(manager.orders)
        self.assertEqual(after, before + 1)

    # 9
    def test_add_multiple_orders_increases_length_correctly(self) -> None:
        """Adding multiple orders should increase length accordingly."""
        manager = RestaurantManager.get_instance()
        manager.add_order(Order(foods=[Pizza()]))
        manager.add_order(Order(foods=[Burger()]))
        manager.add_order(Order(foods=[Pizza(), Burger()]))

        self.assertEqual(len(manager.orders), 3)

    # 10
    def test_orders_content_persists_across_get_instance_calls(self) -> None:
        """Content of orders list must persist across get_instance calls."""
        manager1 = RestaurantManager.get_instance()
        order = Order(foods=[Pizza()])
        manager1.add_order(order)

        manager2 = RestaurantManager.get_instance()
        self.assertIn(order, manager2.orders)

if __name__ == "__main__":
    print("Running tests...")
    unittest.main()
    print("All tests finished.")
