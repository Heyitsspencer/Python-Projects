from abc import ABC, abstractmethod
class car(ABC):
    def paySlip(self,amount):
        print("Your purchase amount: ",amount)
#This functino is telling us to pass in an argument, but we won't tell you
#how or what kind of data it will be.
    @abstractmethod
    def payment(self,amount):
        pass

class DebitCardPayment(car):
#here we've defined how to implement the payment function from its parent
#paySli[ class
    def payment(self,amount):
        print('Your purchase amount of {} exceeded your $100 limit '.format(amount))

obj = DebitCardPayment()
obj.payslip("$400")
obj.payment("$400")
