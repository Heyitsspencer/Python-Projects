
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
class Excersize(Animal):
        morning_excersize = 'Play with carrot toy'
        evening_excersize = 'Go on walk'
