import os

class BankAccount:
    def __init__(self, name, accountType, balance=0):
        self.name = name
        self.accountType = accountType
        self.balance = balance
        
        self.accountNumber = hash(self.name + accountType) % 1000000  
        
        self.filename = f"{self.accountNumber}_{self.accountType}_{self.name}.txt"
        
        with open(self.filename, 'w') as file:
            file.write(f"Initial Balance: {self.balance}\n")
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            with open(self.filename, 'a') as file:
                file.write(f"Deposited: {amount}, New Balance: {self.balance}\n")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            with open(self.filename, 'a') as file:
                file.write(f"Withdrew: {amount}, New Balance: {self.balance}\n")
        else:
            print("Insufficient funds or invalid withdrawal amount.")
    
    def get_balance(self):
        return self.balance
    
    def get_account_number(self):
        return self.accountNumber
    
    def get_account_type(self):
        return self.accountType
    
    def get_user_name(self):
        return self.name
    
    def get_transaction_history(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return file.read()
        else:
            return "No transaction history available."
    
# Create multiple BankAccount objects
account1 = BankAccount("Alice", "savings")
account2 = BankAccount("Bob", "chequing")

# Deposit some money
account1.deposit(500)
account2.deposit(1000)

# Withdraw some money
account1.withdraw(200)
account2.withdraw(500)

# Get balance
print(f"Alice's balance: {account1.get_balance()}")
print(f"Bob's balance: {account2.get_balance()}")

# Get transaction history
print(f"Alice's transaction history:\n{account1.get_transaction_history()}")
print(f"Bob's transaction history:\n{account2.get_transaction_history()}")

# Get account details
print(f"Alice's account number: {account1.get_account_number()}")
print(f"Bob's account number: {account2.get_account_number()}")
print(f"Alice's account type: {account1.get_account_type()}")
print(f"Bob's account type: {account2.get_account_type()}")
