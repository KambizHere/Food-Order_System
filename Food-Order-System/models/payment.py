from dataclasses import dataclass


@dataclass
class Payment:
    """
    Represents payment information.
    """
    amount: float

    def process(self) -> str:
        """
        Processes the payment
        """
        return f"Payment of ${self.amount} processed."
