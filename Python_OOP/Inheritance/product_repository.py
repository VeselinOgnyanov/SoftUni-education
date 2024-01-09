from project.drink import Drink
from project.food import Food
from project.product import Product


class ProductRepository:
    def __init__(self) -> None:
        self.products = []

    def add(self, product:Product):
        self.products.append(product)

    def find(self, product_name: str):
        for current_product in self.products:
            if product_name == current_product.name:
                return current_product

    def remove(self, product_name: str):
        if self.find(product_name):
            self.products.remove(self.find(product_name))

    def __repr__(self) -> str:
        return "\n".join([f"{product}: {product.quantity}"for product in self.products])

# food = Food("apple")
# drink = Drink("water")
# repo = ProductRepository()
# repo.add(food)
# repo.add(drink)
# print(repo.products)
# print(repo.find("water"))
# repo.find("apple").decrease(5)
# print(repo)
