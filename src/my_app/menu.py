from webbshop import main
from Bank_of_Anders import bank_menu


def main_menu():
    active = True
    while active:

        print("\nHuvudmeny\n")
        print("1. Bank of Anders")
        print("2. Webbshop")
        print("0. Exit\n")

        choice = input("Enter your choice: ")

        if choice == "0":
            active = False

        elif choice == "1":
            bank_menu()

        elif choice == "2":
            main()

main_menu()