class Product:
    """Represents a product in a store with price and quantity."""

    def __init__(self, name: str, price: float, quantity: int):
        if not isinstance(name, str):
            raise TypeError("Name must be a string!")
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a number!")
        if not isinstance(quantity, int):
            raise TypeError("Quantity must be an integer!")

        if not name:
            raise ValueError("Name cannot be empty!")
        if price < 0:
            raise ValueError("Price cannot be negative!")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative!")

        self.name: str = name
        self.price: float = price
        self.quantity: int = quantity
        self.active: bool = quantity > 0

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, amount: int):
        if not isinstance(amount, int):
            raise TypeError("Amount must be an integer!")
        if amount < 0:
            raise ValueError("Amount cannot be negative!")
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
        if not isinstance(amount, int):
            raise TypeError("Amount must be an integer!")
        if amount < 0:
            raise ValueError("Amount cannot be negative!")
        if self.quantity < amount:
            raise ValueError("Not enough units available!")
        self.set_quantity(-amount)
        return self.price * amount
