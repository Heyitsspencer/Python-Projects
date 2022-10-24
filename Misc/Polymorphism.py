
#Parent class user
class User:
    name = "Spencer"
    email = "heyitsspencerdavis@gmail.com"
    password = "12345abc"

    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The email or password is incorrect")
#Child class employee
class Employee(User):
    base_pay = 15.00
    department = "General"
    pin_number = "1234"

    #This is the same method in the parent class User
    #The difference is that instead of using entry_password, we're using an entry pin
    def getLoginInfo(self):
        entry_name = input("Enter your name: ")
        entry_pin = input("Enter your pin: ")
        entry_email = input("Enter your email: ")
        if (entry_pin == self.pin_number and entry_email == self.email):
            print("Welcome back, {}!".format(entry_name))
        else:
            print("The pin or email is incorrect")
#Child class customer
class Manager(User):
    base_pay = 20.00
    department = "General"
    pin_number = "2345"
    
    
    



if __name__ == "__main__":
    customer = User()
    customer.getLoginInfo()

    manager = Employee()
    manager.getLoginInfo()
    
