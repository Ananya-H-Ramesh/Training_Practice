import logging
from .cart import Cart
from .products import PRODUCTS

def main():
    cart = Cart()

    cart.add_item("apple")
    cart.add_item("banana")
    cart.add_item("orange")


    items = cart.get_items()
    logging.info("Items in the cart:", items)


    total_price = sum(PRODUCTS[item] for item in items)
    logging.info("Total price:", total_price)