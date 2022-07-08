#5 Lambda Tutorial (Anonymous Function)

def func(x):
    return x + 5

func2 = lambda x: x + 5

def func3(x): # writing mini functions in a bigger function
    func4 = lambda x: x + 5
    return func4(x) + 85 

func5 = lambda x, y: x + y

print("-----Lambda Function-----")
print(func(2))
print(func2(9))
print(func3(3))
print(func5(5, 5))

# using Lambda with Map and Filter

print("\n-----Using Lambda with Map and Filter-----")
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

newList1 = list(map(lambda x: x + 5, a))
newList2 = list(filter(lambda x: x % 2 == 0, a))
print(newList1)
print(newList2)