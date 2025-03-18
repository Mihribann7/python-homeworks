import json

class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

class Bank:
    def __init__(self):
        self.accounts = {}
        self.load_from_file()

    def create_account(self, name, initial_deposit):
        acc_num = len(self.accounts) + 1
        self.accounts[acc_num] = {
            'name': name,
            'balance': initial_deposit
        }
        self.save_to_file()
        print(f"Account {acc_num} has been created")

    def view_account(self, acc_num):
        account = self.accounts.get(acc_num)
        if account:
            print(f"Account {acc_num}, Name: {account['name']}, Balance: ${account['balance']}")
        else:
            print("Account not found.")

    def deposit(self, acc_num, amount):
        if acc_num in self.accounts and amount > 0:
            self.accounts[acc_num]['balance'] += amount
            self.save_to_file()
            print(f"Deposited ${amount}. New balance: ${self.accounts[acc_num]['balance']}")
        else:
            print("Invalid account number or deposit amount.")

    def withdraw(self, account_number, amount):
        if account_number in self.accounts and amount > 0:
            if self.accounts[account_number]['balance'] >= amount:
                self.accounts[account_number]['balance'] -= amount
                self.save_to_file()
                print(f"Withdrew ${amount}. Remaining balance: ${self.accounts[account_number]['balance']}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid account number or withdrawal amount.")

    def save_to_file(self):
        with open("bank_data.json", "w") as file:
            json.dump(self.accounts, file, indent=4)

    def load_from_file(self):
        try:
            with open("bank_data.json", "r") as file:
                self.accounts = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.accounts = {}

bank = Bank()
bank.create_account("Alice", 1000)
bank.create_account("Bob", 500)

bank.view_account(1)
bank.deposit(1, 200)
bank.withdraw(1, 300)

bank.view_account(2)
bank.withdraw(2, 600)
