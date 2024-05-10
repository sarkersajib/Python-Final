import random
class Bank:
    def __init__(self):
      
        self.total_balance = 0
        self.total_loan = 0
        self.loan_status = True
        
        self.account_list = []

    def create_account(self,name,email,address,account_type):
        self.name = name
        self.email = email
        self.address = address
        self.account_type = account_type
        self.account_no = random.randint(1234567,9876543)
        user= (name,email,address,account_type)
        self.transaction_history = []
        self.account_list.append(user)
        print("Account create succcessfully")

    def deposit(self,amount):
        self.total_balance += amount
        print(f"Deposited ${amount}")
        self.transaction_history.append(f"Deposited ${amount}")

    def withdraw(self,amount):
        if self.total_balance > amount:
            self.total_balance -= amount
            print(f"Withdrew ${amount}")
            self.transaction_history.append(f"Withdrew ${amount}")
        else:
            print("Withdrawal amount exceed !")

    def check_balance(self):
        return self.total_balance
        
    def see_transaction_history(self):
        return self.transaction_history
       

    def total_loan(self,amount):
        if self.total_loan < 2:
            self.total_loan +=1
            self.deposit(amount)
            self.transaction_history.append(f"Total loan: ${amount}")

    def transfer(self,amount,recive_account):
        if self.total_balance >= amount:
            recive_account.deposit(amount)
            self.withdraw(amount)
            self.transaction_history.append(f"Balance Transfer: ${amount} to {user_account.account_number}")
        
    def find_account(self,account_no):
        for account in self.account_list:
            if account.account_no == account_no:
                return account

    def bankrupt(self):
        for account in self.account_list:
            total_balance += account.balance
            if total_balance < 0:
                print("Bank is Bankrupt !")



    def __str__(self):
         return f"Name: {self.name}, Account Type: {self.account_type}, Balance: ${self.balance}, Account Number: {self.account_number}"


class Admin:
    def __init__(self,bank):
        self.bank = bank

    def create_account(self,name,email,address,account_type):

        
        self.bank.create_account(name, email, address, account_type)
        
        #
        
    def delete_account(self,account_no):
        if account_no in self.bank.account_list:
            del self.Bank.account_list[account_no]
            print("Account Deleted")
        else:
            print("Account does not exist")

    def show_users(self):
        for user in self.bank.account_list:
            print(user)

    def see_total_balance(self):
        print(f"Total Available Balance:{self.bank.total_balance}")

    def see_total_loan(self):
        print(f"Total Loan:{self.bank.total_loan}")

    def toggle_loan_feature(self,status):
        self.bank.loan_status = status
        print("Loan feature is now", "enabled" if status else "disabled")


bank = Bank()
admin = Admin(bank)   


#bank.create_account("sajib", "sajib@gmail.com", "savar", "Savings")
#bank.deposit( 1000)
#bank.withdraw( 500)
#bank.check_balance()
#bank.total_loan("200")
#bank.transfer(12345, 200)
#bank.see_transaction_history()
#admin.create_account("rajib","rajib@gmail.com","Dhaka","Current")
#admin.show_users()
#admin.see_total_balance()
#admin.toggle_loan_feature(False)








while True:
    print("Option")
    print("1: Admin")
    print("2: User")
    print("3: Exit")

    ch = int(input("Enter Option: "))

    if ch==1:
        print("1: Create Account")
        print("2: Delete Account")
        print("3: All User Account")
        print("4: Total Available Balaance")
        print("5: Total loan amount")
        print("6: Loan Feature")

        op =int(input("Enter OPtion: "))
        if op == 1:
            name = input("Enter Name:")
            email = input("Enter email:")
            address = input("Enter Address:")
            account_type = input("Enter Account_Type:")
            admin.create_account(name,email,address,account_type)

        elif op == 2:
            account_no = input("Enter Account_no: ")
            admin.delete_account(account_no)

        elif op==3:
            admin.show_users()
        elif op==4:
            admin.see_total_balance()
        elif op == 5:
            admin.see_total_loan()
        elif op == 6:
            status = input("Enter Status: ")
            admin.toggle_loan_feature()
        else:
            print("Exit")

    elif ch == 2:

        print("1: Create Account")
        print("2: Check Balance")
        print("3: Check Transaction History")
        print("4: Deposit Amount")
        print("5: Withdraw amount")
        print("6: Total Loan")
        print("7: Transfer Amount")

        op = int(input("Enter OPtion: "))
        if op ==1:
            name = input("Enter Name:")
            email = input("Enter email:")
            address = input("Enter Address:")
            account_type = input("Enter Account_Type:")
            bank.create_account(name,email,address,account_type)
        elif op == 2:
            account_no = input("Enter account_number")
            bank.check_balance()
        elif op == 3:
            bank.see_transaction_history()
        elif op == 4:
            amount = int(input("Enter amount:"))
            bank.deposit(amount)
        elif op == 5 :
            amount = int(input("Enter amount:"))
            bank.withdraw(amount)
        elif op == 6 :
            amount = int(input("Enter amount:"))
            bank.total_loan(amount)
        elif op == 7:
            amount = int(input("Enter amount:"))
            recive_account = input("Enter Recive Account:")
            bank.transfer(amount,recive_account)
        else:
            print("Exit")
    elif ch == 3:
        print("Exit Done")















        

