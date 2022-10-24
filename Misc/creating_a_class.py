class User:
    #Define the attributes of the class
    name = "No name provided"
    email = ""
    password = "1234abcd"
    account = 0

    #Define the methods of the class
    def login(self):
        entry_email = input("Enter your email: ")
        entry_password = input("Enter your password: ")
        if (entry_email == self.email and entry_password == self.password):
            print("Welcome back, {}!".format(self.name))
        else:
            print("You are not authorized for this page")
    #Outside of the class you would create an instance of the User class
    new_user = User()
    #Call the login method using the new object
    new_user.login()

    #Creating a class
    def __init__(animal, name, owner, species, age):
        animal.name = name
        animal.owner = owner
        animal.species = species
        animal.age = age
    New_animal = Animal("Mirabelle", "Spencer","Cat", 7)

    #Creating classes with arguments
    class Animal:
        name = 'Mirabelle'
        owner = 'Spencer'
        species = 'cat'
        age = 7
    class Diet(Animal):
        morning_food = '1/4 can wet'
        evening_food = '1/4 cup dry'
    class Excersize(User):
        morning_excersize = 'Play with carrot toy'
        evening_excersize = 'Go on walk'
