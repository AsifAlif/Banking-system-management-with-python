class user:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def show_details_of_user(self):
        print(f"{self.name}'s details: ",)
        print("Age: ",self.age)
        print("Gender: "+self.gender)
class Bank(user):
    def __init__(self,name,age,gender):
        super().__init__(name,age,gender)
        self.balance=0
    def Deposit(self,ammount):
        self.ammount=ammount
        self.balance=self.balance+self.ammount
        print(f"You have deposited Tk {self.ammount} balance")
        print(f"Now your new balance is : {self.balance} Tk")
    def Witdraw(self,ammount):
        self.ammount=ammount
        if self.ammount > self.balance:
            print("Insufficent balance")
            print("Balance available :",self.balance)
        else:
            self.balance=self.balance-self.ammount
            print(f"Your new balance is {self.balance} Tk")
    def Loan(self,ammount):
        self.ammount=ammount
        self.interest=self.ammount/100
        print(f"The interest for Tk {self.ammount} Loan is Tk{self.interest} per month")
    def view_balance(self):
        self.show_details_of_user()
        print("Account balance is Tk",self.balance)
name=input("Enter user name : ")
age=int(input("Enter user age: "))
gender=input("Enetr user Gender: ")
user1=Bank(name,age,gender)
ammount=int(input("Enter The ammount you want to Deposit : "))
user1.Deposit(ammount)
ammount=int(input("Enter the ammount you want to witdraw : "))
user1.Witdraw(ammount)
ammount=int(input("Enetr the ammount you want to take loan: "))
user1.Loan(ammount)
user1.view_balance()



