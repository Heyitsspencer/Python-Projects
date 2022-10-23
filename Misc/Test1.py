
def getInfo():
    var1 = input("Please provide the first numeric value: ")
    var2 = input("Please provide the second numeric value: ")
    return var1,var2

def compute(var1,var2):
    go = true
    while go:
        var1,var2 = getInfo()
        try:
            var3 = int(var1) + int(var2)
            print("{} + {} = {}".format(var1, var2, var3))
            go = False
        except ValueError as e:
            print("{}: \nYou did not provide a numeric value!".format(e))
        except:
            print("Oops you provided invalid input, the program will close now")
    print("{} + {} = {}".fomat(var1,var2,var3))
    


if __name__ == "__main__":
    compute(var1,var2)
