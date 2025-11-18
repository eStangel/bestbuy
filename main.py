import store
from products import Product

# setup initial stock of inventory
product_list = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250)
]
best_buy = store.Store(product_list)


def list_products(best_buy):
    items = best_buy.get_all_products()
    if items:
        for i in range(len(items)):
            print(
                f"{i + 1}: {items[i].name}, Price: ${items[i].price}, "
                f"Quantity: {items[i].quantity}"
            )
    else:
        print("\nStore sold out!")


def get_total_amount(best_buy):
    total_amount = best_buy.get_total_quantity()
    print(f"Total of {total_amount} items in store")


def get_order(best_buy):
    print("------")
    list_products(best_buy)
    print("------\n"
        "When you want to finish order, enter empty text.")
    length_product_list = len(best_buy.get_all_products())
    is_item = True
    shopping_list = []
    while is_item:
        product_number = input("Which product # do you want? ")
        if product_number:
            try:
                if not 1 <= int(product_number) <= length_product_list:
                    print(f"Enter a number (1-{length_product_list})")
                    continue
                product_number = int(product_number)
            except ValueError:
                print("Enter a number!")
                continue

        amount = input("What amount do you want? ")
        items = best_buy.get_all_products()
        if amount:
            try:
                if not 1 <= int(amount) <= items[product_number - 1].quantity:
                    print(f"Enter a number (1-{items[product_number - 1].quantity})")
                    continue
                amount = int(amount)
            except ValueError:
                print("Enter a number!")
                continue

        if product_number and amount:
            # Checks if items of product were already included in order and if so,
            # updates quantity of items accordingly
            item_updated = False
            if shopping_list:
                for item in range(len(shopping_list)):
                    if items[product_number - 1] == shopping_list[item][0]:
                        if (shopping_list[item][1] + amount) <= items[product_number - 1].quantity:
                            shopping_list[item] = shopping_list[item][0], shopping_list[item][1] + amount
                        else:
                            print("Not enough items of this product available "
                                  f"({items[product_number - 1].quantity} max)")
                        item_updated = True
            if not item_updated:
                shopping_list.append((items[product_number - 1], amount))
        else:
            if shopping_list:
                payment = best_buy.order(shopping_list)
                print(f"Order made! Total payment: ${payment}")
            is_item = False


def start(best_buy):

    while True:
        print(
            "\n   Store Menu"
            "\n   ----------"
            "\n1. List all products in store\n"
            "2. Show total amount in store\n"
            "3. Make an order\n"
            "4. Quit\n"
        )

        try:
            command = input("Please choose a number: ")
            if not 1 <= int(command) <= 4:
                print("Command must be a number (1-4)!")
            else:
                run_command, args = COMMANDS[command]
                run_command(*args)
        except ValueError:
            print("Command must be a number!")


COMMANDS = {
    "1": (list_products, [best_buy]),
    "2": (get_total_amount, [best_buy]),
    "3": (get_order, [best_buy]),
    "4": (exit, [])
}


if __name__ == "__main__":
    start(best_buy)
