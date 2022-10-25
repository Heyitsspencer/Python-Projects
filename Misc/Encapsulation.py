#Protected variable
class Protected:
    def __init__(self):
        self.protectedVar = 0
    obj = Protected()
    obj._protectedVar = 25
    print(obj.protectedVar)
#Output wil be 25

#Private variable, private + protected
class Protected1:
    def __init__(self):
        self.privateVar = 12

    def getPrivate(self):
        print(self._privateVar)

    def setPrivate(self, private):
        self.__privateVar = private
obj= Protected()
obj.getPrivate()
obj.setPrivate(23)
obj.getPrivate()
#Output will be:
#12
#23
