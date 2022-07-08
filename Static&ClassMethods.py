#2 Static and Class Methods

class person(object):
    population = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod # call it on any instance of a class, object is not required to be created, accesses anything in the class with 'cls'
    def getPopulation(cls):
        return cls.population
    
    @staticmethod # can be called without using a class, parameters not necessary, do not need 'self', cannot access 'population'
    def isAdult(age):
        return age >= 18

    def display(self):
        print(self.name, 'is', self.age, "years old.")

print("-----Static & Class Methods-----")
newPerson = person('Zach', 28)

print(person.getPopulation()) # object not created and not needed to do this

print(person.isAdult(5))
print(person.isAdult(21))
newPerson.display()