from abc import ABC, abstractmethod
class abs_class(ABC):
    #normal method
    def print(self,x):
        print("Passed value: ",x)
        #method definition
    @abstractmethod
    def task(self):
        print("We are inside Absclass task")

class test_class(abs_class):
    def task(self):
        print("We are inside test_class task")

class example_class(abs_class):
    def task(self):
        print("We are inside example_class task")

#object of test_class created
test_obj = test_class()
test_obj.task()
test_obj.print(100)

#object of exmample_class created
example_obj = example_class()
example_obj.task()
example_obj.print(200)

print("test_obj is instance of Absclass? ", isinstance(test_obj,abs_class))
print("example_obj is instance of Absclass? ", isinstance(example_obj,abs_class))
        
