class CheckingAccount:
    def __init__(self, name, address, accountsNumber, balance=0.00):
        self.name = name
        self.address = address
        self.accountNumber = accountsNumber
        self._balance = balance

    def credit(self, amount):
        """make a deposit - credit operation"""
        self._balance += amount
        print("Amount Deposited: ", amount)

    def debit(self, amount):
        """make a withdrawal - debit operation"""
        if self._balance >= amount:
            self._balance -= amount
            print("You withdraw: ",amount)
        else:
            print("Insufficient Fund")
        
        # if amount > self._balance:
        #     raise ValueError("Insufficient funds")
        # self._balance -= amount

    @property
    def balance(self):
        """check the balance"""
        return self._balance

    def __repr__(self):
        return '\nchecking Account: \nFull Name: {} \nAddress: {} \nAccounts Number: {}'.format(self.name, self.address, self.accountNumber)        

    def __str__(self):
        return 'Current Balance: ${:.2f}'.format(self.balance)       
          
#===========Driver program========
#create an object of CheckingAccount
    
customer1 = CheckingAccount("Saba Ephrem", "Spring Street 20857", "36162848")
print(repr(customer1))

customer1.credit(100)
customer1.debit(30)
print(customer1) #checking balance after withdrawal

customer1.debit(90) #trying to withdraw more than available balance
print(customer1)

customer1.debit(60) #withdraw an ampunt less than the available balance
print(customer1)

