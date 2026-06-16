
class Customer:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number

customer_1 = Customer("John", "Doe", "john.doe@gmail.com", "123456")


class Product:
    """ En produkt i webbutiken. Produkt-id, pris, namn, lagersaldo."""

    def __init__(self, product_id, price, name, inventory):
        self.__id = product_id
        self.name = name
        self.price = price
        self.inventory = inventory

    def __str__(self):
        return f"{self.name}: {self.price} kr, {self.inventory} i lager. Det totala värdet är {self.__stock_value()} kr."


    def __stock_value(self):
        return self.inventory * self.price

produkt_1 = Product(1337, 500, "Skruvdragare", 20)
produkt_2 = Product(1338, 299, "Hammare", 40)
produkt_3 = Product(1339, 599, "Vinkelslip", 7)


class Order:
    """En order i webbutiken. Order_id, Customer"""

    def __init__(self, order_id, customer, order_lines=None):
        self.__id = order_id
        self.status = 'pending'
        self.total = 0
        self.customer = customer
        self.order_lines = []


    def add_order_line(self, product, quantity):
        """Lägg till en order kundvagnen. Produkt, quantity."""
        self.order_lines.append(product.name)
        self.total += product.price * quantity
        product.inventory -= quantity

    def remove_order_line(self, product, quantity):
        """Ta bort en produkt ur kundvagnen. Produkt, quantity."""
        self.order_lines.remove(product.name)
        self.total -= product.price * quantity
        product.inventory += quantity


    def print_order(self):
        """Visa ordern."""
        print(f"\nCustomer ID: {self.__id}\nCustomer name: {self.customer.first_name}\nPris: {self.total}\nProdukter: {self.order_lines}\n")

    def order_line_contain(self):
        x = self.order_lines
        print(x)
        print(f"\n {self.customer.first_name} : {self.order_lines}")



def main():
    active = True
    products = f"\n{produkt_1.name}: {produkt_1.price} kr.\n{produkt_2.name}: {produkt_2.price} kr.\n{produkt_3.name}: {produkt_3.price} kr.\n"
    order_1 = Order(1337, Customer("John", "Doe", "", "123456"))


    while active:
        print("\nShopping Cart Menu\n")
        print("1. Products")
        print("2. Add order")
        print("3. Print order")
        print("4. Remove order")
        print("0. Exit")

        choice = input("\nEnter your choice: ")


        if choice == "0":
            active = False

        elif choice == "1":
            print(products)

        elif choice == "2":
            print(f"\nLägg till en produkt i kundvagnen")
            print("1. Skruvdragare")
            print("2. Hammare")
            print("3. Vinkelslip")
            print("0. Exit\n")

            choice_2 = input("Enter your choice: ")
            if choice_2 == "1":
                order_1.add_order_line(product=produkt_1, quantity=1)
            elif choice_2 == "2":
                order_1.add_order_line(product=produkt_2, quantity=1)
            elif choice_2 == "3":
                order_1.add_order_line(product=produkt_3, quantity=1)


        elif choice == "3":
            order_1.print_order()

        elif choice == "4":
            print(f"\nTa bort en produkt ur kundvagnen")
            print("1. Skruvdragare")
            print("2. Hammare")
            print("3. Vinkelslip")
            print("0. Exit\n")

            choice_3 = input("Enter your choice: ")

            if choice_3 == "0":
                main()

            elif choice_3 == "1":
                if produkt_1.name in order_1.order_lines:
                    order_1.remove_order_line(product=produkt_1, quantity=1)
                else:
                    print("Produkten finns inte i din kundvagn.")
            elif choice_3 == "2":
                if produkt_2.name in order_1.order_lines:
                    order_1.remove_order_line(product=produkt_2, quantity=1)
                else:
                    print("Produkten finns inte i din kundvagn.")
            elif choice_3 == "3":
                if produkt_3.name in order_1.order_lines:
                    order_1.remove_order_line(product=produkt_3, quantity=1)
                else:
                    print("Produkten finns inte i din kundvagn.")
