

class BankKonto:

    def __init__(self):
        self.balance = 0

    def __str__(self):
        return "Välkommen till Anders Bank!"

    def deposit(self):
        amount = float(input("Ange hur mycket du vill sätta in: "))
        self.balance += amount
        return f"Du har satt in {amount} kr på ditt konto. Ditt saldo är nu {self.balance} kr."


    def withdraw(self):
        amount = float(input("Ange hur mycket du vill ta ut: "))
        if self.balance < amount:
            return f"Du kan inte ta ut så mycket. Ditt saldo är {self.balance} kr."
        else:
            self.balance -= amount
        return f"Du har tagit ut {amount} kr från ditt konto. Ditt saldo är {self.balance} kr."


    def account_balance(self):
        return f"Ditt saldo är {self.balance} kr."


    def interest(self):
        return f"Din ränta ligger på 0.0%"


    def enough_balance(self):
        amount = float(input("Ange hur mycket du ska betala: "))
        if self.balance < amount:
            return False
        else:
            return True


z = BankKonto()


def bank_menu():
    active = True
    while active:
        print(f"\n{z}\n")
        print(f"1. Saldo")
        print(f"2. Sätt in pengar")
        print(f"3. Ta ut pengar")
        print(f"4. Kontrollera om du har råd med en räkning")
        print(f"5. Ränta")
        print(f"\n0 - Avsluta\n")

        control = input("\nSelect an option: ")

        if control == "0":
            active = False

        elif control == "1":
            print(f"\n{z.account_balance()}")

        elif control == "2":
            print(z.deposit())

        elif control == "3":
            print(z.withdraw())

        elif control == "4":
            print(z.enough_balance())

        elif control == "5":
            print(z.interest())
