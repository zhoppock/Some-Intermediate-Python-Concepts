#1 Optional Parameters 

# Tutorial #1
print("-----Optional Parameter Tutorial #1-----")

def func1(x = 1):
    return x ** 2

call = func1(5)
print(call)
call = func1()
print(call)


# Optional Parameters Tutorial #2
print("\n-----Optional Parameter Tutorial #2-----")

def func2(word, add = 5, freq = 1):
    print(word * (freq + add))

func2('hello')
func2('hello', 0)
func2('hello', 5, 3)

#swap the last two parameters but leave the examples the same
def func3(word, freq = 5, add = 1):
    print(word*(freq+add))

func3('hello')
func3('hello', 0)
func3('hello', 5, 3)


# Optional Parameters Tutorial #3
print("\n-----Optional Parameter Tutorial #3-----")

class car(object):
    def __init__(self, make, model, year, condition = 'New', kms = 0):
        self.make = make
        self.model = model
        self.year = year
        self.condition = condition
        self.kms = kms
    
    def display(self, showAll=True):
        if showAll:
            print("This car is a %s %s from %s, it is %s and has %s kms." % (self.make, self.model, self.year, self.condition, self.kms))
        else:
            print("This car is a %s %s from %s." % (self.make, self.model, self.year))

whip1 = car('Ford', 'Fusion', 2012)
whip1.display(False)
whip2 = car('Honda', 'Civic', 2015, 'Used', 10000)
whip2.display()