# programming_paradigm/bank_account.py

class BankAccount:
    """A simple BankAccount class that supports deposit, withdrawal, and balance display."""

    def __init__(self, initial_balance=0):
        """Initialize the account with an optional initial balance."""
        self.__account_balance = initial_balance  # Private attribute for encapsulation

    def deposit(self, amount):
        """Deposit the specified amount into the account."""
        if amount > 0:
            self.__account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw the specified amount if funds are sufficient. Returns True if successful."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.__account_balance}")
