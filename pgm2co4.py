
class Bank:
    def __init__(self, accno, name, acctype, balance):
        self.accno = accno
        self.name = name
        self.acctype = acctype
        self.balance = balance

    def deposit(self, amt):
        self.balance += amt
        print("Amount Deposited. New Balance =", self.balance)

    def withdraw(self, amt):
        if amt > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amt
            print("Amount Withdrawn. New Balance =", self.balance)


# User Input
accno = input("Enter Account Number: ")
name = input("Enter Name: ")
acctype = input("Enter Account Type: ")
balance = float(input("Enter Initial Balance: "))

b = Bank(accno, name, acctype, balance)

b.deposit(float(input("Enter amount to deposit: ")))
b.withdraw(float(input("Enter amount to withdraw: ")))
