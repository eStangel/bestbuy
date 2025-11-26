from products import Product


class Store:
    """
    Represents a store and provides methods for making an inventory of its
    products and handling orders.
    """

    def __init__(self, product_list: list):
        if not isinstance(product_list, list):
            raise TypeError("Product list must be a list!")
        if not product_list:
            raise ValueError("Products must contain at least one item!")
        self.products = product_list

    def add_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Product must be an instance of class Product!")
        self.products.append(product)

    def remove_product(self, product: Product):
        if not isinstance(product, Product):
            raise TypeError("Product must be an instance of class Product!")
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> list[Product]:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        return sum(item[0].buy(item[1]) for item in shopping_list)

