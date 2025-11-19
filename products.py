class Product:
    """Represents a product in a store with price and quantity."""

    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Name cannot be empty!")
        if price < 0:
            raise ValueError("Price cannot be negative!")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative!")

        self.name: str = name
        self.price: float = price
        self.quantity: int = quantity
        self.active: bool = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, amount: int):
        if self.quantity + amount < 0:
            raise ValueError("Quantity cannot be negative!")
        self.quantity += amount
        if self.quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, amount: int) -> float:
        if self.quantity < amount:
            raise ValueError("Not enough units available!")
        self.set_quantity(-amount)
        return self.price * amount
