
class Customer:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

customer_1 = Customer("John", "Doe", "john.doe@gmail.com", "123456")


class Product:
    def __init__(self, product_id, price, name, inventory):
        self.__id = product_id
        self.name = name
        self.price = price
        self.inventory = inventory

    def __str__(self):
        return f"{self.name}: {self.price} kr, {self.inventory} i lager. Det totala värdet är {self.__stock_value()} kr."


    def __stock_value(self):
        return self.inventory * self.price

skruvdragare = Product(1337, 500, "Skruvdragare", 20)
hammare = Product(1338, 299, "Hammare", 40)
vinkelslip = Product(1339, 599, "Vinkelslip", 7)


class Order:
    def __init__(self, order_id, customer):
        self.__id = order_id
        self.status = 'pending'
        self.total = 0
        self.customer = customer
        self.order_line = []


    def print_order(self):
        print(self.__id, self.customer.first_name, self.total, self.order_line)


    def add_order(self, product, quantity):
        self.add_order(product, quantity)
        self.total += product.price * quantity
        product.inventory -= quantity


#order_1 = Order(1, customer_1)
#order_2 = Order(2, 31)
#order_3 = Order(3, 32)

class ShoppingCart:
    def __init__(self, shopping_cart_id):
        self.items = {}
        self.__id = shopping_cart_id


order_1 = Order(1337, Customer("John", "Doe", "", "123456"))
order_1.print_order()
#order_1.add_order(product=skruvdragare, quantity=1)
#order_1.print_order()


#print(skruvdragare)
#print(hammare)
#print(vinkelslip)
