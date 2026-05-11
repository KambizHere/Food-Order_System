"Kambiz Shiri"

from patterns.singleton import RestaurantManager
from patterns.factory_method import PizzaFactory, BurgerFactory, SaladFactory
from patterns.builder import OrderBuilder
from models.payment import Payment
from models.notification import Notification


def main() -> None:
    print("FOOD ORDER SYSTEM")
    print("--------------------------------")

    pizza = PizzaFactory().create_food()
    burger = BurgerFactory().create_food()
    salad = SaladFactory().create_food()

    print(pizza.prepare())
    print(burger.prepare())
    print(salad.prepare())

    builder = OrderBuilder()
    order = builder.add_food(pizza).add_food(burger).add_food(salad).build()

    manager = RestaurantManager.get_instance()
    manager.add_order(order)

    print(order.summary())

    payment = Payment(amount=45.0)
    print(payment.process())

    note = Notification("Your order is ready!")
    print(note.send())

    print(f"Orders in system: {len(manager.orders)}")


if __name__ == "__main__":
    main()


