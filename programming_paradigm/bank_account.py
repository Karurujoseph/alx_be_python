# programming_paradigm/bank_account.py

class BankAccount:
    def __init__(self, balance=0.0):
        """Initialize a new bank account with an optional starting balance."""
        if balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.__balance = balance  # Private attribute for encapsulation

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.__balance += amount
        print(f"Deposited ${amount:.2f}")

    def withdraw(self, amount):
        """Withdraw a positive amount if sufficient balance is available."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.__balance:
            print("Insufficient funds.")
            return False
        self.__balance -= amount
        print(f"Withdrew ${amount:.2f}")
        return True

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current balance: ${self.__balance:.2f}")

    def get_balance(self):
        """Getter method for the balance (if needed)."""
        return self.__balance

