from dataclasses import dataclass


@dataclass
class Notification:
    """
    Sends user notifications regarding the order
    """
    message: str

    def send(self) -> str:
        return f"Notification sent: {self.message}"
