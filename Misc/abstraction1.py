from abc import ABC
class abs_class(ABC):
    #normal method
    def print(self,x):
        print("Passed value: ",x)
        #method definition
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")

class test_class(Absclass):
    def task(self):
        print("We are inside test_class task")

class example_class(Absclass):
    def task(self):
        print("We are inside example_class tasj")

#object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)

#object of exmample_class created
example_obj = example_class()
example_obj.task()
example_obj.print(200)

print("test_obj is instance of Absclass? ", isinstance(test_obj,Absclass))
print("example_obj is instance of Absclass? ", isinstance(example_obj,Absclass))
        
