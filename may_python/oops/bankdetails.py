class Bank:
    acno=int
    balance=int
    ac_type=str
    p_name=str


    def create_account(self,acno,balance,ac_type,p_name):
        self.acno=acno
        self.balance=balance
        self.ac_type=ac_type
        self.p_name=p_name

    def deposit(self,amount):
        self.balance+=amount
        print(f"your sbk acount {self.acno} has been credited with amount {amount} aval balance is{self.balance}")

    def withdraw(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            print(f"your sbk acount {self.acno} has been debited with amount {amount} aval balance is{self.balance}")
        else:
            print("transaction failed insufficient balance")

obj1=Bank()
obj1.create_account(1234,20000,"joint","aruna")
# obj1.deposit(1000)
obj1.withdraw(1000)